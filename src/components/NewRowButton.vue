<template>
    <button @click="onClick" class="pure-button pure-button-active">
        {{ text }}
    </button>
</template>

<script>
export default {
    name: 'NewRowButton',
    props: {
        text: String
    },
    methods: {
        onClick () {
            console.log('click')
            this.$emit('btn-click')
        }
    }
}
</script>
