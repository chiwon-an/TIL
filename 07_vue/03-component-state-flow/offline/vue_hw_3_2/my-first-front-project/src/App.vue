<script setup>
import ChildCard from './components/ChildCard.vue'
</script>

<template>
  <div style="border: 2px solid #bbb; margin: 16px; padding: 16px;">
    <div style="border: 2px solid #ccc; padding: 32px;">
      <h1 style="font-size: 2.5rem; font-weight: bold; margin-bottom: 32px;">부모 페이지입니다.</h1>
      <ChildCard name="김하나" age="30" />
      <ChildCard name="김두리" age="20" />
      <ChildCard name="김서이" age="10" />
    </div>
  </div>
</template>

<style>
/* Optional: global styles */
</style>
