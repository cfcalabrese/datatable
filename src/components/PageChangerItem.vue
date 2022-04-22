<template>
    <div class="w-full items-center justify-center grid grid-cols-5 px-1 bg-slate-700 rounded-b">
        <i class="hover:text-sky-400 hover:text-xl text-slate-800 fa-solid fa-angles-left pl-3 justify-self-start cursor-pointer" @click="changePage(-1)" />
        <i class="hover:text-sky-400 hover:text-xl text-slate-800 fa-solid fa-angle-left pl-3 justify-self-start cursor-pointer" @click="changePage(-5)" />
        <div class="px-5 self-center justify-self-center text-sm text-center rounded text-black font-bold m-1 bg-white">
            {{ pageNumber }}
        </div>
        <i class="hover:text-sky-400 hover:text-xl text-slate-800 fa-solid fa-angle-right justify-self-end pr-3 cursor-pointer" @click="changePage(1)" />
        <i class="hover:text-sky-400 hover:text-xl text-slate-800 fa-solid fa-angles-right self-center justify-self-end pr-3 cursor-pointer" @click="changePage(5)" />
    </div>
</template>

<script>
export default {
    name: 'PageChangerItem',
    props: {
        pageNumber: Number
    },
    methods: {
        changePage (increment) {
            this.$emit('change-page', increment)
        }
    }
}
</script>
