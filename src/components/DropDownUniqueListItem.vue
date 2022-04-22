<template>
    <div class="w-full">
        <div class="grid grid-cols-4">
            <input 
                class="col-span-4 pl-2 w-full text-sm rounded text-white p-1 border focus:ring-3 focus:ring-blue-300 bg-gray-800 border-gray-600 focus:ring-blue-600 ring-offset-gray-800" 
                type="text"
                v-model="filterValue"
                @input="sendFilterValue(); showOn()"
                :placeholder="text"
                @click="showOn"
            >
            <i 
                class="fas fa-times hover:text-red-600 text-white cursor-pointer absolute z-20 self-center justify-self-end mr-3"
                @click="clearField(); showOff; sendFilterValue()"
            />
        </div>
        <div class="absolute z-10 min-w-[24%]">
            <select v-show="show" v-model="filterValue" class="pl-2 w-full text-sm rounded text-white p-1 border focus:ring-3 focus:ring-blue-300 bg-gray-800 border-gray-600 focus:ring-blue-600 ring-offset-gray-800">
                <option @click="sendFilterValue(); toggleShow()" />
                <option 
                    @click="sendFilterValue(); toggleShow()" 
                    v-for="(val, index) in uniqueVals"
                    :key="index"
                >
                    {{ val }}
                </option>
            </select>
        </div>
    </div>
</template>

<script>
export default {
    name: 'DropDownUniqueListItem',
    data () {
        return {
            filterValue: '',
            show: false
        }
    },
    props: {
        uniqueVals: Array,
        class: String,
        text: String,
        id: String
    },
    methods: {
        clearField () {
            this.filterValue = ''
            this.show = false
        },
        toggleShow () {
            this.show = !this.show
        },
        showOn () {
            this.show = true
        },
        showOff (e) {
            if (!this.$el.contains(e.target)) {
                this.show = false
            }
        },
        sendFilterValue () {
            let uniqueVal = this.filterValue
            this.$emit('filter', uniqueVal)
        },
        showDropDown (filterValue) {
            if (filterValue) {
                return true
            } else {
                return false
            }
        }
    },
    created () {
        window.addEventListener('click', this.showOff)
    },
    beforeDestroy () {
       window.removeEventListener('click', this.showOff) 
    },
    emits: ['filter']
}
</script>
