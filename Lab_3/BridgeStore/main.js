import SpringSummerCollection from './SpringSummerCollection';
import FallWinterCollection from './FallWinterCollection';
import Pants from './Pants';
import Shirt from './Shirt';
import Sweater from './Sweater';
import TShirt from './TShirt';
import ClothingItem from './ClothingItem';

// Створення екземплярів класів
const springSummerCollection = new SpringSummerCollection();
const fallWinterCollection = new FallWinterCollection();
const pants = new Pants();
const shirt = new Shirt();
const sweater = new Sweater();
const tShirt = new TShirt();

// Створення товарів
const items = [
  new ClothingItem(pants, springSummerCollection, "\"Жовтий пляж\"", 'images/pants_1.jpeg'),
  new ClothingItem(pants, springSummerCollection, "\"Cиній пляж\"", 'images/pants_2.jpeg'),
  new ClothingItem(shirt, springSummerCollection, "\"Жовта паті\"", 'images/shirt_1.jpeg'),
  new ClothingItem(shirt, springSummerCollection, "\"Синій ананас\"", 'images/shirt_2.jpeg'),
  new ClothingItem(tShirt, springSummerCollection, "\"Літо вже тут\"", 'images/t-shirt_1.jpg'),
  new ClothingItem(tShirt, springSummerCollection, "\"Серфінг\"", 'images/t-shirt_2.jpg'),
  new ClothingItem(sweater, springSummerCollection, "\"Три полоски\"", 'images/sweater_1.png'),
  new ClothingItem(sweater, springSummerCollection, "\"П'ять полосок\"", 'images/sweater_2.jpg'),
  new ClothingItem(pants, fallWinterCollection, "\"Сірий вовк\"", 'images/pants_3.jpg'),
  new ClothingItem(pants, fallWinterCollection, "\"Невгамовний олень\"", 'images/pants_4.jpg'),
  new ClothingItem(shirt, fallWinterCollection, "\"Перший сніг\"", 'images/shirt_3.png'),
  new ClothingItem(shirt, fallWinterCollection, "\"Різдв'яний скала\"", 'images/shirt_4.png'),
  new ClothingItem(tShirt, fallWinterCollection, "\"Різдв'яний кіт\"", 'images/t-shirt_3.png'),
  new ClothingItem(tShirt, fallWinterCollection, "\"Санта Клаус\"", 'images/t-shirt_4.png'),
  new ClothingItem(sweater, fallWinterCollection, "\"Мисливець\"", 'images/sweater_3.png'),
  new ClothingItem(sweater, fallWinterCollection, "\"Непохитний вовк\"", 'images/sweater_4.png'),
];

document.addEventListener('DOMContentLoaded', function() {
  const itemsContainer = document.getElementById('clothing-items');
  const similarTypeList = document.getElementById('similar-type');
  const similarCollectionList = document.getElementById('similar-collection');

  function showSimilarTypeItems(selectedItem) {
    const similarItems = selectedItem.getSimilarItems(items);
    similarTypeList.innerHTML = similarItems.map(item => `<li>${item.getDescription()}</li>`).join('');
  }

  function showSimilarCollectionItems(selectedItem) {
    const sameCollectionItems = selectedItem.getItemsFromSameCollection(items);
    similarCollectionList.innerHTML = sameCollectionItems.map(item => `<li>${item.getDescription()}</li>`).join('');
  }

  itemsContainer.innerHTML = items.map((item, index) => `
  <div class="item-container" data-index="${index}">
    <div class="clothing-item">
      <img src="${item.imageURL}" alt="${item.getDescription()}">
      <p>${item.getDescription()}</p>
    </div>
  </div>
`).join('');

  itemsContainer.addEventListener('click', function(event) {
  const target = event.target.closest('.item-container');
  if (target) {
    const index = parseInt(target.dataset.index);
    const selectedItem = items[index];
    showSimilarTypeItems(selectedItem);
    showSimilarCollectionItems(selectedItem);
  }
});

});
