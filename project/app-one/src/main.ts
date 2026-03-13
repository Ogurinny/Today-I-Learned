// src/main.ts

interface Todo {
  id: number
  text: string
  done: boolean
}

const todos: Todo[] = []

const input = document.querySelector<HTMLInputElement>("#input")!
const list = document.querySelector<HTMLUListElement>("#list")!
const btn = document.querySelector<HTMLButtonElement>("#btn")!

function render(): void {
  list.innerHTML = todos
    .map(todo => `
      <li style="text-decoration: ${todo.done ? 'line-through' : 'none'}">
        ${todo.text}
      </li>
    `)
    .join("")
}

btn.addEventListener("click", () => {
  if (!input.value.trim()) return

  todos.push({
    id: Date.now(),
    text: input.value,
    done: false
  })

  input.value = ""
  render()
})
