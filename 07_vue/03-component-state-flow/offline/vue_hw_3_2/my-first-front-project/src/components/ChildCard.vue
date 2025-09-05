<template>
  <div style="border: 1px solid #bbb; padding: 24px; margin-bottom: 16px; background: #fff;">
    <h2 style="font-size: 1.2rem; font-weight: bold; margin-bottom: 12px;">자식 페이지입니다.</h2>
    <div>이름 : {{ name }}</div>
    <div>나이 : {{ age }}</div>
  </div>
</template>

<script>
export default {
  name: 'ChildCard',
  props: {
    name: {
      type: String,
      required: true
    },
    age: {
      type: [String, Number],
      required: true
    }
  }
}
</script>

<style scoped>
/* Optional: component-specific styles */
</style>