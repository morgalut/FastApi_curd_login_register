import React, { useState, useEffect } from 'react';
import TaskForm from '../components/TaskForm';
import TaskList from '../components/TaskList';
import { getTasks, createTask, Task, CreateTaskDTO } from '../api/taskApi';

const TasksPage: React.FC = () => {
    const [tasks, setTasks] = useState<Task[]>([]);

    useEffect(() => {
        const fetchTasks = async () => {
            const fetchedTasks = await getTasks();
            setTasks(fetchedTasks);
        };
        fetchTasks();
    }, []);

    const handleAddTask = async (newTask: CreateTaskDTO) => {
        const createdTask = await createTask(newTask);
        setTasks((prevTasks) => [...prevTasks, createdTask]);
    };

    const handleUpdateTask = (updatedTask: Task) => {
        setTasks((prevTasks) =>
            prevTasks.map((task) =>
                task.id === updatedTask.id ? updatedTask : task
            )
        );
    };

    const handleDeleteTask = (taskId: number) => {
        setTasks((prevTasks) => prevTasks.filter((task) => task.id !== taskId));
    };

    return (
        <div>
            <h2>Task Manager</h2>
            <TaskForm onAddTask={handleAddTask} />
            <TaskList tasks={tasks} onTaskUpdate={handleUpdateTask} onTaskDelete={handleDeleteTask} />
        </div>
    );
};

export default TasksPage;
