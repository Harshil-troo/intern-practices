//fetch('https://jsonplaceholder.typicode.com/todos/55')
//      .then(response => response.json())
//      .then(json => console.log(json))

let options = {
    method : "POST",
    headers :{
        'content-type' : 'application/json'
    },
    body: JSON.stringify({
    title: 'foo',
    body: 'bar',
    userId: 1,
  })
}

fetch('https://jsonplaceholder.typicode.com/posts', options)
  .then((response) => response.json())
  .then((json) => console.log(json));