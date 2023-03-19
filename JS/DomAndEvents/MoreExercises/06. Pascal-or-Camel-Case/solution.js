function solve() {
  const txt = document.querySelector('#text');
  const outputType = document.querySelector('#naming-convention');
  const output = document.querySelector('#result')
  const start = {
    'Camel Case': 1,
    'Pascal Case': 0
  }

  if (txt && outputType) {
    let words = txt.value.toLowerCase().split(' ');
    
      if (!start.hasOwnProperty(outputType.value)) {
        output.textContent = 'Error!'
      } else {
        for (let i = start[outputType.value]; i < words.length; i++) {
          words[i] = `${words[i][0].toUpperCase()}${words[i].slice(1)}`
        }
        output.textContent = words.join('')
      }
    
  }
}