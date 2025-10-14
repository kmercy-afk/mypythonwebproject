<template>
<div>
    <el-col :span="12">
    <el-card class="box-card" shadow="hover" style="margin: 5px 0;">
        <el-row :gutter="12">
        <el-col :span="21">{{ title }}</el-col>
        <el-col :span="3">
            <el-button @click="removeItem" circle icon="el-icon-check" type="success"></el-button>
        </el-col>
        </el-row>
    </el-card>
    </el-col>
</div>
</template>

<script>
export default {
name: 'TodoItem',
props: {
    title: String,
    index: Number
},
methods: {
    removeItem() {
    this.$emit('remove', this.index);
    }
}
};
</script>