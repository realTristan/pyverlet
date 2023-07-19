#ifndef TESTING_VERLET_MENU_HPP
#define TESTING_VERLET_MENU_HPP

#include <objects/verlet/ball/colliders/circle.hpp>
#include <objects/verlet/ball/colliders/line.hpp>
#include <objects/verlet/ball/ball.hpp>
#include <interface/menu.hpp>
#include <testing/events.hpp>
#include <testing/config.hpp>
#include <testing/utils.hpp>
#include <SFML/Graphics.hpp>
#include <grid/grid.hpp>
#include <vector>

#define CIRCLE_COLLIDER_POSITION Vec2D<float>(400, 300)
#define CIRCLE_COLLIDER_RADIUS 300
#define CIRCLE_COLLIDER_THICKNESS 2
#define CIRCLE_COLLIDER_COLOR WHITE

#define LINE_COLLIDER_VECTOR Vec2D<float>(200, 250)
#define LINE_COLLIDER_LENGTH 150
#define LINE_COLLIDER_ANGLE 60
#define LINE_COLLIDER_WIDTH 2
#define LINE_COLLIDER_COLOR WHITE

#define VERLET_BALL_COUNT 600
#define VERLET_BALL_VECTOR Vec2D<float>(200, 200)
#define VERLET_BALL_RADIUS 4
#define VERLET_BALL_ADD_INTERVAL 100 // 100ms
#define VERLET_BALL_OFFSET Vec2D<float>(0, 0)
#define VERLET_BALL_RANDOM_COLOR true

typedef std::vector<VerletBall *> VerletBallVector;

class MenuTesting
{
public:
    static void start()
    {
        // Initialize a new window
        sf::RenderWindow *window = new sf::RenderWindow(
            sf::VideoMode(WINDOW_WIDTH, WINDOW_HEIGHT), WINDOW_TITLE);
        window->setFramerateLimit(60);

        // Create a new list of colliders
        CircleCollider *circle_collider = new CircleCollider(
            CIRCLE_COLLIDER_POSITION,
            CIRCLE_COLLIDER_RADIUS,
            CIRCLE_COLLIDER_THICKNESS);
        
        circle_collider->set_outline_color(CIRCLE_COLLIDER_COLOR);
        circle_collider->disable_outside_collision();

        LineCollider *line_collider = new LineCollider(
            LINE_COLLIDER_VECTOR,
            LINE_COLLIDER_LENGTH,
            LINE_COLLIDER_ANGLE,
            LINE_COLLIDER_WIDTH,
            LINE_COLLIDER_COLOR);

        // Create a new list of balls
        VerletBallVector balls = VerletBallVector();
        Utils::auto_add_verlet_balls(
            &balls,
            VERLET_BALL_VECTOR,
            VERLET_BALL_COUNT,
            VERLET_BALL_RADIUS,
            VERLET_BALL_ADD_INTERVAL,
            VERLET_BALL_OFFSET,
            VERLET_BALL_RANDOM_COLOR);

        // Menu variables
        Menu *menu = new Menu();
        bool show_circle_collider = false;
        bool show_line_collider = false;

        // Window Loop
        while (window->isOpen())
        {
            Events::check_close(window);
            Utils::draw_background(window);

            // Draw the menu
            menu->draw(window);

            // Check if the menu buttons have been clicked
            if (menu->circle_collider_button->is_clicked(window))
            {
                show_circle_collider = !show_circle_collider;
            }
            if (menu->line_collider_button->is_clicked(window))
            {
                show_line_collider = !show_line_collider;
            }

            // Draw the circle collider
            if (show_circle_collider)
            {
                circle_collider->draw(window);
            }

            // Draw the line collider
            if (show_line_collider)
            {
                line_collider->draw(window);
            }

            // Draw and update the balls
            for (int i = 0; i < SUBSTEPS; i++)
            {
                for (int j = 0; j < balls.size(); j++)
                {
                    balls[j]->draw(window);
                    balls[j]->update(window, &balls);

                    // Draw the circle collider
                    if (show_circle_collider)
                    {
                        circle_collider->apply(balls[j]);
                    }

                    // Draw the line collider
                    if (show_line_collider)
                    {
                        line_collider->apply(balls[j]);
                    }
                }
            }

            // Update the window
            window->display();
        }
    }
};

#endif