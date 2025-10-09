<template>
<div>
    <h1>todo list</h1>
    <!-- todo input form -->
    <form @submit.prevent="addTodo()">
    <el-input placeholder="todo" v-model="todo"></el-input>
    </form>
    <el-row :gutter="12">
    <!-- todo display area -->
    <todoitem 
        :key="index" 
        :todo="todoItem" 
        :index="index"
        @remove="removeTodo"
        v-for="(todoItem, index) in todos"
    ></todoitem>
    <!-- Issue Display Area -->
    <el-col :key="issue.id" :span="12" v-for="(issue, index) in issues">
        <el-card class="box-card" shadow="hover" style="margin: 5px 0;">
        <el-row :gutter="12">
            <el-col :span="21">{{ issue.title }}</el-col>
            <el-col :span="3">
            <el-button @click="closeIssue(index)" circle icon="el-icon-check" type="success"></el-button>
            </el-col>
        </el-row>
        </el-card>
    </el-col>
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
        });
    },
    getIssues() {
    client.get('issues')
        .then((res) => {
        this.issues = res.data;
        });
    }
},
created() {
    this.getIssues();
}
};
</script>