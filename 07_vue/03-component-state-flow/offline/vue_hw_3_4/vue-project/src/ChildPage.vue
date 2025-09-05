<template>
  <div>
    <h2>자식 페이지입니다.</h2>
    <p>이름 : {{ name }}</p>
    <p>나이 : {{ age }}</p>
    <p>용돈 : {{ money }}</p>
    <button @click="askMoney">용돈 주세요.</button>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'
const props = defineProps({
  name: String,
  age: Number,
  money: Number
})

function askMoney() {
  alert('용돈 주세요.')
}
</script>

<style scoped>
div {
  border: none;
  margin-bottom: 20px;
}
h2 {
  font-size: 20px;
  color: #222;
}
</style>
