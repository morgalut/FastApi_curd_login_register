import React, { useState } from 'react';
import { CreateTaskDTO } from '../api/taskApi';

interface TaskFormProps {
    onAddTask: (task: CreateTaskDTO) => Promise<void>;
}

const TaskForm: React.FC<TaskFormProps> = ({ onAddTask }) => {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [priority, setPriority] = useState('medium');

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        const newTask: CreateTaskDTO = { title, description, priority };
        await onAddTask(newTask);
        setTitle('');
        setDescription('');
        setPriority('medium');
    };

    return (
        <form onSubmit={handleSubmit}>
            <input 
                type="text" 
                value={title} 
                onChange={(e) => setTitle(e.target.value)} 
                placeholder="Task Title" 
                required 
            />
            <textarea 
                value={description} 
                onChange={(e) => setDescription(e.target.value)} 
                placeholder="Task Description" 
                required 
            />
            <select value={priority} onChange={(e) => setPriority(e.target.value)}>
                <option value="low">Low</option>
                <option value="medium">Medium</option>
                <option value="high">High</option>
            </select>
            <button type="submit">Add Task</button>
        </form>
    );
};

export default TaskForm;
