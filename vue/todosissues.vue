<template>
<div>
    <h1>todo list</h1>
    <!-- todo input form -->
    <form @submit.prevent="addTodo()">
    <el-input placeholder="todo" v-model="todo"></el-input>
    </form>
    <el-row :gutter="12">
    <!-- todo display area -->
    <TodoItem 
        :key="index" 
        :title="todoItem" 
        :index="index"
        @remove="removeTodo"
        v-for="(todoItem, index) in todos"
    ></TodoItem>
    <!-- Issue Display Area -->
    <TodoItem 
        :key="issue.id" 
        :title="issue.title" 
        :index="index"
        @remove="closeIssue"
        v-for="(issue, index) in issues"
    ></TodoItem>
    </el-row>
</div>
</template>

<script>
import axios from 'axios';
import TodoItem from '@/components/TodoItem';

const client = axios.create({
baseURL: `${process.env.VUE_APP_GITHUB_ENDPOINT}`,
headers: {
    'Authorization': `token ${process.env.VUE_APP_GITHUB_TOKEN}`,
    'Accept': 'application/vnd.github.v3+json',
    'Content-Type': 'application/json',
},
});

export default {
name: 'TodosIssues',
components: {
    TodoItem
},
data() {
    return {
    todo: '',
    todos: [],
    issues: []
    };
},
methods: {
    addTodo() {
    this.todos.push(this.todo);
    this.todo = '';
    },
    removeTodo(index) {
    this.todos.splice(index, 1);
    },
    closeIssue(index) {
    const target = this.issues[index];
    client.patch(`/issues/${target.number}`, { state: 'closed' })
        .then(() => {
        this.issues.splice(index, 1);
        })
        .catch((error) => {
        console.error('Error closing issue:', error);
        });
    },
    getIssues() {
    client.get('/issues')
        .then((res) => {
        this.issues = res.data.filter(issue => issue.state === 'open');
        });
    }
},
created() {
    this.getIssues();
}
};
</script>