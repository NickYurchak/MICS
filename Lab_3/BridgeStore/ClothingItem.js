// Клас ClothingItem містить тип, колекцію та посилання на зображення
export default class ClothingItem {
    constructor(clothingType, collection, name, imageURL) {
      this.clothingType = clothingType;
      this.collection = collection;
      this.name = name;
      this.imageURL = imageURL;
    }
  
    getDescription() {
      return `${this.clothingType.getType()} з коллекції ${this.collection.getCollection()}, ${this.name}`
    }
  
    // Оновлений метод, що повертає список товарів такого ж типу
    getSimilarItems(items) {
      const similarItems = items.filter(item => item !== this && item.clothingType.getType() === this.clothingType.getType());
      return similarItems;
    }
  
    // Оновлений метод, що повертає список всіх товарів із такою ж колекцією
    getItemsFromSameCollection(items) {
      const sameCollectionItems = items.filter(item => item !== this && item.collection.getCollection() === this.collection.getCollection());
      return sameCollectionItems;
    }
  }

module.exports = ClothingItem;

