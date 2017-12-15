function highlight(terms) {
  const escapedSearchStr = terms.map(escapeRegExpInput).join('|');
  const regex = new RegExp(`\\b(${escapedSearchStr})\\b`, 'i');
  $(document).markRegExp(regex, {
    acrossElements: true,
    separateWordSearch: true
  });
} 

function escapeRegExpInput(input) {
  return input.replace(/([.*+?^${}()|\[\]\/\\])/g, "\\$1");
}