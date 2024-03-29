
import numpy as np


def de_casteljau(t, control_net, return_diagonals=False):
    """
    Returns a point on the Bezier curve respect a given parameter.

    This function applies de Casteljau algorithm, using a
    constructive approach (ie, the geometric one).

    Given a control net, it produces a tuple (p, ud, ld) such that:
        - p is the point on the Bezier curve that interpolate the control net;
        - ud is an array containing points on the upper diagonal for curve splitting;
        - ld is an array containing points on the lower diagonal for curve splitting.
    Observe that to get the triple with diagonals, the argument `return_diagonals`
    should be set to `True`, otherwise only a point is returned.

    This function is persistent respect the given control net, ie it doesn't
    change the given net but, working on a copy of it (requires little extra time to
    make a copy of it, this is included in big-O complexity).

    The overall complexity is O(n^2), where n is the number of control points.
    """

    n, d = dimensions = np.shape(control_net)

    Q = np.copy(control_net)

    upper_diagonal = np.empty(dimensions)
    lower_diagonal = np.empty(dimensions)

    upper_diagonal[0, :] = Q[0, :]
    lower_diagonal[0, :] = Q[-1, :]

    for k in range(1, n):

        for i in range(n - k): Q[i, :] = (1 - t) * Q[i, :] + t * Q[i + 1, :]

        upper_diagonal[k, :] = Q[0, :]
        lower_diagonal[k, :] = Q[-(k + 1), :]

    point = Q[0, :]

    return (point, upper_diagonal, lower_diagonal) if return_diagonals else point


def de_casteljau_surface(params, control_net):
    """
    Produces a point on the Bezier surface.

    Examples
    ========

    The following example works on a square control net:
    The 9 cotrol points from : " cele 9 puncte de control (din spatiu!);"
    >>> b00 = np.array([0, 0, 0])
    >>> b01 = np.array([2, 0, 0])
    >>> b02 = np.array([4, 0, 0])
    >>> b10 = np.array([0, 2, 0])
    >>> b11 = np.array([2, 2, 0])
    >>> b12 = np.array([4, 2, 2])
    >>> b20 = np.array([0, 4, 0])
    >>> b21 = np.array([2, 4, 4])
    >>> b22 = np.array([4, 4, 4])
    >>> control_net = np.array([[b00,b01,b02],\
                                [b10,b11,b12],\
                                [b20,b21,b22]], dtype="float")
    >>> u,v = .5, .5
    >>> point = de_casteljau_surface((u,v), control_net)
    >>> point
    array([2., 2., 1.])
    """

    control_net = np.copy(control_net)

    u, v = params

    rows, cols, d = np.shape(control_net)

    square = min(rows, cols)

    def combine_col(r, c):
        return (1 - v) * control_net[r, c, :] + v * control_net[r, c + 1, :]

    def combine_row(r, c):
        return (1 - u) * control_net[r, c, :] + u * control_net[r + 1, c, :]

    #   Combine the largest square in the control net from the top-left corner
    for k in range(square - 1):
        for r in range(square - k):
            for c in range(square - k - 1): control_net[r, c, :] = combine_col(r, c)

            # after the previous loops we've eliminated the rightmost column
        for c in range(square - k - 1):
            for r in range(square - k - 1): control_net[r, c, :] = combine_row(r, c)

    point = control_net[0, 0, :]

    if cols > square:
        #       Combine remaining cols if any, using de Casteljau algorithm for curve case

        def de_casteljau_on_col(c):
            return de_casteljau(u, control_net[:, c, :])

        intermediate_row = np.array([de_casteljau_on_col(c)
                                     for c in range(square - 1, cols)])

        point = de_casteljau(v, np.vstack((point, intermediate_row)))

    elif rows > square:
        #       Combine remaining rows if any, using de Casteljau algorithm for curve case

        def de_casteljau_on_row(r):
            return de_casteljau(v, control_net[r, :, :])

        intermediate_col = np.array([de_casteljau_on_row(r)
                                     for r in range(square - 1, rows)])

        point = de_casteljau(u, np.vstack((point, intermediate_col)))

    else:
        pass  # square control net already handled

    return point


def naive_de_casteljau(control_net, tabs=None, squares_per_dim=20):
    """
    Naive implementation of de Casteljau algorithm for tensor product patches.
    """

    squares_per_dim *= 10

    if tabs is None:
        tabs = (np.linspace(0, 1, squares_per_dim),
                np.linspace(0, 1, squares_per_dim))

    X, Y = tabs

    X, Y = np.meshgrid(X, Y)

    surface = np.array([de_casteljau_surface((u, v), control_net)
                        for u, v in zip(np.ravel(X), np.ravel(Y))])

    return surface, X.shape


def vectorized_de_casteljau(control_net, tabs=None, squares_per_dim=20):
    """
    Vectorized implementation of de Casteljau algorithm for tensor product patches.
    """

    squares_per_dim *= 10

    if tabs is None:
        tabs = (np.linspace(0, 1, squares_per_dim),
                np.linspace(0, 1, squares_per_dim))

    u_tab, v_tab = tabs

    #   Sestini's code calls `m` what we call `rows` and
    #   calls `n` what we call `cols`.
    rows, cols, d = np.shape(control_net)

    k = min(rows, cols)
    mtab, ntab = len(u_tab), len(v_tab)
    u_tab, v_tab = np.meshgrid(u_tab, v_tab)
    shape = u_tab.shape
    u_tm, v_tm = 1 - u_tab, 1 - v_tab

    surface = np.zeros((mtab, ntab, d, rows, cols))

    def initialize(it, jt, i_d):
        surface[it, jt, i_d, :, :] = control_net[:, :, i_d]

    [initialize(it, jt, i_d) for it in range(mtab)
     for jt in range(ntab)
     for i_d in range(d)]

    def update_square(i_d, i, j):
        uv_tm_tm = np.multiply(u_tm, v_tm)
        uv_tm_tab = np.multiply(u_tm, v_tab)
        uv_tab_tm = np.multiply(u_tab, v_tm)
        uv_tab_tab = np.multiply(u_tab, v_tab)
        surface[:, :, i_d, i, j] = (
                np.multiply(uv_tm_tm, surface[:, :, i_d, i, j])
                + np.multiply(uv_tm_tab, surface[:, :, i_d, i, j + 1])
                + np.multiply(uv_tab_tm, surface[:, :, i_d, i + 1, j])
                + np.multiply(uv_tab_tab, surface[:, :, i_d, i + 1, j + 1]))

    #   Combine in square block as much as `k` allow
    for s in range(1, k):
        [update_square(i_d, i, j) for i_d in range(d)
         for i in range(rows - s)
         for j in range(cols - s)]

    def update_along_u(i_d, i):
        surface[:, :, i_d, i, 0] = (np.multiply(u_tm, surface[:, :, i_d, i, 0]) +
                                    np.multiply(u_tab, surface[:, :, i_d, i + 1, 0]))

    #   Complete combining along `u` direction if any
    for r in range(rows - k):
        [update_along_u(i_d, i) for i_d in range(d)
         for i in range(rows - k - r)]

    def update_along_v(i_d, j):
        surface[:, :, i_d, 0, j] = (np.multiply(v_tm, surface[:, :, i_d, 0, j]) +
                                    np.multiply(v_tab, surface[:, :, i_d, 0, j + 1]))

    #   Complete combining along `v` direction if any
    for c in range(cols - k):
        [update_along_v(i_d, j) for i_d in range(d)
         for j in range(cols - k - c)]

    #   Clean parameterization values away from `surface` structure
    surface = np.array([surface[i, j, :, 0, 0] for i in range(mtab)
                        for j in range(ntab)])

    return surface, shape