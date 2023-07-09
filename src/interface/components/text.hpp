#include <iostream>
#include <physics/vector2d.hpp>
#include <utils/colors.hpp>
#include <SFML/Graphics.hpp>

#ifndef INTERFACE_COMPONENTS_TEXT_HPP
#define INTERFACE_COMPONENTS_TEXT_HPP

class Text
{
private:
    std::string text;
    Vec2D position;
    int size;
    Color color = WHITE;

public:
    Text(std::string text, Vec2D position, int size, Color color = WHITE)
    {
        this->text = text;
        this->position = position;
        this->size = size;
        this->color = color;
    }

    // Draw the text
    void draw(sf::RenderWindow *window)
    {
        sf::Font font;
        font.loadFromFile("assets/fonts/arial.ttf");
        sf::Text text(this->text, font);
        text.setCharacterSize(this->size);
        text.setFillColor(Colors::to_sf(this->color));
        text.setPosition(sf::Vector2f(this->position.x, this->position.y));
        window->draw(text);
    }
};

#endif // INTERFACE_COMPONENTS_TEXT_HPP