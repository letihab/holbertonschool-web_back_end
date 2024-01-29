// returns a string of all the set values that start with a specific string

export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') {
    return '';
  }
  const newSet = [];

  set.forEach((item) => {
    if (typeof item === 'string' && item.startsWith(startString)) {
      newSet.push(item.slice(startString.length));
    }
  });

  return newSet.join('-');
}
