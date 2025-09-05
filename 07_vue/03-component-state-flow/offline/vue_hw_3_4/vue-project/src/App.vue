
<script setup>
import { ref } from 'vue'
import ChildPage from './ChildPage.vue'

const children = ref([
  { name: '김하나', age: 30, money: 102000 },
  { name: '김두리', age: 20, money: 12000 },
  { name: '김세이', age: 10, money: 4000 },
])
</script>

<template>
  <div>
    <h1>부모 페이지입니다.</h1>
    <div v-for="child in children" :key="child.name">
      <ChildPage :name="child.name" :age="child.age" :money="child.money" />
    </div>
  </div>
</template>

<style scoped>
div {
  border: 1px solid #ccc;
  padding: 10px;
  margin-top: 10px;
}
h1 {
  font-size: 36px;
}
h2 {
  font-size: 20px;
  color: #222;
}
h3 {
  font-size: 18px;
}
p {
  font-size: 14px;
}
</style>
