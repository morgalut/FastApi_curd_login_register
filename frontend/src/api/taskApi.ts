import axios from 'axios';

const API_URL = 'http://localhost:8000'; // Update with the correct URL

export interface Task {
    id: number;
    title: string;
    description: string;
    status: string;
    priority: string;
}

export interface CreateTaskDTO {
    title: string;
    description: string;
    priority: string;
}

export const getTasks = async () => {
    const response = await axios.get<Task[]>(`${API_URL}/tasks`);
    return response.data;
};

export const createTask = async (task: CreateTaskDTO) => {
    const response = await axios.post<Task>(`${API_URL}/tasks`, task);
    return response.data;
};

export const updateTaskStatus = async (taskId: number, status: string) => {
    const response = await axios.patch<Task>(`${API_URL}/tasks/${taskId}/status`, { status });
    return response.data;
};

export const updateTask = async (taskId: number, task: Partial<CreateTaskDTO>) => {
    const response = await axios.put<Task>(`${API_URL}/tasks/${taskId}`, task);
    return response.data;
};

export const deleteTask = async (taskId: number) => {
    await axios.delete(`${API_URL}/tasks/${taskId}`);
};
