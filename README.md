# Restaurant Chatbot

The Restaurant Chatbot is a virtual assistant built with the Rasa framework to support restaurant-related conversations. It is designed to help customers interact naturally, place orders, check food prices, view the restaurant interior, and ask general or emotional questions.

---

## 💬 What It Can Do

This chatbot can:

- Greet and say goodbye to customers politely.
- Recognize and respond to customer mood, including happy or unhappy sentiments.
- Handle both serious requests and casual chitchat.
- Provide food price details when asked.
- Allow users to place orders by specifying dish names and quantities.
- Respond with a breakdown of the items currently in an order.
- Show the total price of an order.
- Let users search for food items.
- Remove specific food items from an ongoing order.
- Show an image of the restaurant when requested.
- Handle irrelevant or confusing messages gracefully.
- Answer frequently asked questions using a separate FAQ module.

---

## 🧠 How It Works

The chatbot is built using Rasa and leverages custom logic to manage and respond to user interactions. It uses:

- **Slots** to store the user’s food selections, quantities, full order, and total price during a conversation.
- **Entities** extracted from the conversation such as dish names and quantities.
- **Custom Actions** to perform specific tasks like placing an order or returning pricing information.
- **Predefined Responses** for common intents such as greetings or emotional replies.

---

## 🔧 Technologies Used

- **Rasa Framework**: Handles natural language understanding and dialogue management.  
  → [https://rasa.com](https://rasa.com)
- **Custom Python Actions**: For dynamic functions like calculating order total or filtering dishes.
- **Image Responses**: Enhances user experience by showing the restaurant’s ambiance.

---

## 🔁 Session Management

- Sessions automatically expire after 60 minutes of inactivity.
- User data (like current order) is preserved across sessions for a seamless experience.

---

## 🚀 Future Ideas

- Integrate with a live food ordering system.
- Support multiple languages (e.g., English and Vietnamese).
- Add voice interaction.
- Connect to messaging platforms (Zalo, Facebook Messenger, etc).