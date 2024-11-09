// Імпорт класу HandleCounter з файлу counter.js для управління лічильником товарів
import { initCounter} from "/static/js/counter.js";

// Імпорт функції showToast з файлу notifications.js для відображення спливаючих повідомлень
import { showToast } from "/static/js/notifications.js";

// Імпорт класу CartClient з файлу cart-client.js для взаємодії з кошиком товарів
import { CartClient } from "/static/js/cart-client.js";

// Очікування завантаження документа перед ініціалізацією функцій
document.addEventListener("DOMContentLoaded", () => {
  initCounter('.product-decrement-btn', '.product-increment-btn'); // Виклик функції ініціалізації лічильника
  initAddToCart(); // Виклик функції ініціалізації додавання до кошика
});

// Функція ініціалізації додавання товару до кошика
function initAddToCart() {
  const cart = new CartClient(); // Створити екземпляр класу CartClient для роботи з кошиком
  const form = document.querySelector('#add-to-cart-form'); // Знайти форму додавання товару до кошика
  form.addEventListener('submit', (e) => { // Додати обробник події відправки форми
    e.preventDefault(); // Заборонити стандартну поведінку відправки форми

    // Перевірити, чи обрані розмір і колір товару перед додаванням до кошика
    const sizeSelected = form.querySelector('input[name="size"]:checked');
    const colorSelected = form.querySelector('input[name="color"]:checked');
    if (!sizeSelected || !colorSelected) {
      return showToast('Будь ласка, оберіть розмір та колір перед додаванням до кошика', 'warning'); // Показати спливаюче повідомлення, якщо не обрано розмір або колір
    }
    cart.add.bind(cart)(e); // Викликати метод додавання товару до кошика, прив'язаний до об'єкту cart
  });
}