import { useEffect, useState } from "react";

function App() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/tasks")
      .then(res => res.json())
      .then(data => setTasks(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h1>Interview Trainer</h1>

      <ul>
        {tasks.map(task => (
          <li key={task.id}>
            {task.title} ({task.difficulty})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;