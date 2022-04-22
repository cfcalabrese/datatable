<template>
    <div class="group">
        <input 
            :type="type"
            v-model="filterValue"
            :class="class"
            @input="sendFilterValue"
            :placeholder="placeholder"
        >
    </div>
</template>

<script>
export default {
    name: "DropDownItem",
    props: {
        placeholder: String,
        type: String,
        class: String,
    },
    data () {
        return {
            filterValue: ''
        }
    },
    methods: {
        sendFilterValue () {
            this.$emit('filter', this.filterValue)
        }
    },
    emits: ['filter']
}
</script>