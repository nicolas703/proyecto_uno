const sortNames = (names) => { return (names.map(name => name.toLowerCase()).sort()) }

var names = ['John', "julio", 'Kenny', 'Tom', "Bob", 'Dilan']
console.log(sortNames(names))