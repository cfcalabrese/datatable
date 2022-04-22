<template>
    <button @click="onClick()" class="rounded shadow-md bg-slate-800 px-2 py-2 hover:bg-gray-400 text-white font-bold text-sm">
        {{ text }}
    </button>
</template>

<script>
export default {
    name: 'ButtonItem',
    props: {
        text: String
    },
    methods: {
        onClick () {
            this.$emit('btn-click')
        }
    }
}
</script>