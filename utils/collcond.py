def block(obj_pos, screen_edge, direction):
    """ Compatible only with pixelized grid and square objects"""
    if obj_pos.x == screen_edge[0] - 1 and direction == "right":
        obj_pos.x = - 1
    elif obj_pos.x == 0 and direction == "left":
        obj_pos.x = screen_edge[0]
    elif obj_pos.y == screen_edge[1] - 1 and direction == "down":
        obj_pos.y = - 1
    elif obj_pos.y == 0 and direction == "up":
        obj_pos.y = screen_edge[1]
    return obj_pos.x, obj_pos.y
