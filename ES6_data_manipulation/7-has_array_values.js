// 7-set_has_values.js

export default function hasValuesFromArray(set, array) {
  // Use the every method to check if all elements in the array exist in the set
  return array.every((element) => set.has(element));
}
 