<template>
    <button @click="onClick()" class="pure-button pure-button-primary">
        Submit
    </button>
</template>

<script>
export default {
    name: 'SubmitButton',
    methods: {
        onClick () {
            console.log('Submit')
            this.$emit('btn-click')
        }
    }
}
</script>