#ifndef VERLET_BALL_COLLIDERS_CIRCLE_HPP
#define VERLET_BALL_COLLIDERS_CIRCLE_HPP

#include <physics/vector2d.hpp>
#include <utils/colors.hpp>

class CircleCollider
{
public:
    Vec2D position;
    Vec2D center;
    float radius;
    Color color = WHITE;

    CircleCollider(Vec2D position, float radius, Color color = WHITE)
    {
        this->position = position;
        this->radius = radius;
        this->color = color;
    }
};

#endif // CIRCLE_COLLIDER_HPP