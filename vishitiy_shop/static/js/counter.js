class BaseCounter {
  decrement(counter) {
    if (counter.value > 1) {
      counter.value--;
      this.triggerEvent(counter);
    }
  }

  increment(counter) {
    if (counter.value < 10) {
      counter.value++;
      this.triggerEvent(counter);
    }
  }

  triggerEvent(counter) {
    const event = new Event('input', {
      bubbles: true,
      cancelable: true,
    });
    counter.dispatchEvent(event);
  }

  handleEvent(e) {
    const counter = e.target.parentElement.querySelector('[data-id="counter"]');
    if (e.target.dataset.id === 'increment') {
      this.increment(counter);
    } else if (e.target.dataset.id === 'decrement') {
      this.decrement(counter);
    }
  }
}

class HandleCounter extends BaseCounter {
  constructor(decrementButton, incrementButton) {
    super();
    this.decrementButton = decrementButton;
    this.incrementButton = incrementButton;
    this.decrementButton.addEventListener('click', this.handleEvent.bind(this));
    this.incrementButton.addEventListener('click', this.handleEvent.bind(this));
  }
}

class HandleManyCounters extends BaseCounter {
  constructor(incrementButtons, decrementButtons) {
    super();
    this.decrementButtons = decrementButtons;
    this.incrementButtons = incrementButtons;
    this.decrementButtons.forEach(btn => btn.addEventListener('click', this.handleEvent.bind(this)));
    this.incrementButtons.forEach(btn => btn.addEventListener('click', this.handleEvent.bind(this)));
  }
}

// Функція ініціалізації лічильника товарів
function initCounter(decrSelector, incrSelector) {
  const decrementButton = document.querySelector(decrSelector); 
  const incrementButton = document.querySelector(incrSelector); 
  new HandleCounter(decrementButton, incrementButton); // Створити екземпляр класу HandleCounter для управління лічильником
}

export { HandleCounter, HandleManyCounters, initCounter };