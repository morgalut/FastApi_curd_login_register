import React from 'react';
import { Task, updateTask, deleteTask } from '../api/taskApi';

interface TaskListProps {
    tasks: Task[];
    onTaskUpdate: (updatedTask: Task) => void;
    onTaskDelete: (taskId: number) => void;
}

const TaskList: React.FC<TaskListProps> = ({ tasks, onTaskUpdate, onTaskDelete }) => {
    const handleEdit = async (taskId: number) => {
        const updatedTask = prompt("Edit task title:");
        if (updatedTask) {
            const task = await updateTask(taskId, { title: updatedTask });
            onTaskUpdate(task);
        }
    };

    const handleDelete = async (taskId: number) => {
        if (window.confirm("Are you sure you want to delete this task?")) {
            await deleteTask(taskId);
            onTaskDelete(taskId);
        }
    };

    return (
        <ul>
            {tasks.map((task) => (
                <li key={task.id}>
                    <strong>{task.title}</strong> - {task.description} - {task.priority}
                    <button onClick={() => handleEdit(task.id)}>Edit</button>
                    <button onClick={() => handleDelete(task.id)}>Delete</button>
                </li>
            ))}
        </ul>
    );
};

export default TaskList;
