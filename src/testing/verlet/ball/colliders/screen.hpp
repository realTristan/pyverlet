#ifndef TESTING_VERLET_BALL_COLLIDERS_SCREEN_HPP
#define TESTING_VERLET_BALL_COLLIDERS_SCREEN_HPP

#include <objects/verlet/ball/colliders/screen.hpp>
#include <objects/verlet/ball/ball.hpp>
#include <objects/limiter.hpp>
#include <testing/events.hpp>
#include <testing/config.hpp>
#include <testing/utils.hpp>
#include <SFML/Graphics.hpp>
#include <vector>

#define VERLET_BALL_COUNT 50
#define VERLET_BALL_POSITION Vec2D<float>(200.0f, 200.0f)
#define VERLET_BALL_RADIUS 10.0f
#define VERLET_BALL_ADD_INTERVAL 100 // 100ms
#define VERLET_BALL_OFFSET Vec2D<float>(10.0f, 0.0f)
#define VERLET_BALL_RANDOM_COLOR true

typedef std::vector<VerletBall *> VerletBallVector;

// Screen Collider Testing Class
class ScreenColliderTesting
{
public:
    static void start()
    {
        // Initialize a new window
        sf::RenderWindow *window = new sf::RenderWindow(
            sf::VideoMode(WINDOW_WIDTH, WINDOW_HEIGHT), WINDOW_TITLE);
        window->setFramerateLimit(FPS);

        // Create a new list of balls
        VerletBallVector balls = VerletBallVector();
        Utils::auto_add_verlet_balls(
            &balls,
            VERLET_BALL_POSITION,
            VERLET_BALL_COUNT,
            VERLET_BALL_RADIUS,
            VERLET_BALL_ADD_INTERVAL,
            VERLET_BALL_OFFSET,
            VERLET_BALL_RANDOM_COLOR);

        // Create a screen collider
        ScreenCollider screen_collider = ScreenCollider(WINDOW_WIDTH, WINDOW_HEIGHT);

        // Create a new limiter
        ObjectLimiter *limiter = new ObjectLimiter(VERLET_BALL_COUNT);

        // Window Loop
        while (window->isOpen())
        {
            Events::check_close(window);
            Utils::draw_background(window);

            // Add a ball on button click
            Utils::add_verlet_ball_on_click(
                window,
                &balls,
                VERLET_BALL_RADIUS,
                VERLET_BALL_RANDOM_COLOR);

            // Update the limiter
            limiter->update(&balls);

            // Draw and update the balls
            for (int i = 0; i < SUBSTEPS; i++)
            {
                for (int j = 0; j < balls.size(); j++)
                {
                    balls[j]->draw(window);
                    balls[j]->update(window, &balls);
                    screen_collider.apply(balls[j]);
                }
            }

            // Update the window
            window->display();
        }
    }
};

#endif // TESTING_VERLET_BALL_COLLIDERS_SCREEN_HPP