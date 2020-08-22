import math

drag = 0.999
elasticity = 0.75
gravity = (math.pi, 0.002)


"""def add_vectors(angle1, length1, angle2, length2):
    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1) * length1 + math.cos(angle2) * length2

    angle = 0.5 * math.pi - math.atan2(y, x)
    length = math.hypot(x, y)

    return angle, length"""


def collide(p1, p2):
    dx = p1.pos_x - p2.pos_x
    dy = p1.pos_y - p2.pos_y

    distance = math.hypot(dx, dy)
    if distance < p1.size + p2.size:
        angle = math.atan2(dy, dx) + 0.5 * math.pi
        total_mass = p1.mass + p2.mass

        """"(p1.angle, p1.velocity) = add_vectors(p1.angle, p1.velocity * (p1.mass - p2.mass) / total_mass, angle,
                                              2 * p2.velocity * p2.mass / total_mass)

        (p2.angle, p2.velocity) = add_vectors(p2.angle, p2.velocity * (p2.mass - p1.mass) / total_mass,
                                              angle + math.pi, 2 * p1.velocity * p1.mass / total_mass)"""
        p1.velocity *= elasticity
        p2.velocity *= elasticity

        overlap = 0.5 * (p1.size + p2.size - distance + 1)
        p1.pos_x += math.sin(angle) * overlap
        p1.pos_y -= math.cos(angle) * overlap
        p2.pos_x -= math.sin(angle) * overlap
        p2.pos_y += math.cos(angle) * overlap


"""def combine(p1, p2):
    if math.hypot(p1.x - p2.x, p1.y - p2.y) < p1.size + p2.size:
        total_mass = p1.mass + p2.mass
        p1.x = (p1.x * p1.mass + p2.x * p2.mass) / total_mass
        p1.y = (p1.y * p1.mass + p2.y * p2.mass) / total_mass
        (p1.angle, p1.speed) = add_vectors(p1.angle, p1.speed * p1.mass / total_mass,
                                           p2.angle, p2.speed * p2.mass / total_mass)
        p1.speed *= (p1.elasticity * p2.elasticity)
        p1.mass += p2.mass
        p1.collide_with = p2"""
