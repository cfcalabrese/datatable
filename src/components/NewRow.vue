<template>
    <form @submit="onSubmit" class="pt-1 text-sm w-full flex-row flex-nowrap items-center justify-center">
        <input
            type="text"
            name="site-id"
            v-model="id"
            placeholder="AUDATEX_SITE_ID"
            class="rounded text-white p-1 border focus:ring-3 focus:ring-blue-300 bg-gray-800 border-gray-600 focus:ring-blue-600 ring-offset-gray-800 w-1/6"
        />
        <input
            type="text"
            name="garage-name"
            v-model="garageName"
            placeholder="GARAGE_NAME"
            class="rounded text-white p-1 border focus:ring-3 focus:ring-blue-300 bg-gray-800 border-gray-600 focus:ring-blue-600 ring-offset-gray-800 w-1/6"
        />
        <input
            type="text"
            name="approval-type"
            v-model="approvalType"
            placeholder="APPROVAL_TYPE"
            class="rounded text-white p-1 border focus:ring-3 focus:ring-blue-300 bg-gray-800 border-gray-600 focus:ring-blue-600 ring-offset-gray-800 w-1/6"
        />
        <input
            type="text"
            name="approval-subtype"
            v-model="approvalSubType"
            placeholder="APPROVAL_SUBTYPE"
            class="rounded text-white p-1 border focus:ring-3 focus:ring-blue-300 bg-gray-800 border-gray-600 focus:ring-blue-600 ring-offset-gray-800 w-1/6"
        />
        <input
            type="date"
            name="start-date"
            v-model="startDate"
            placeholder="START_DATE"
            class="rounded text-white p-1 border focus:ring-3 focus:ring-blue-300 bg-gray-800 border-gray-600 focus:ring-blue-600 ring-offset-gray-800 w-1/6"
        />
        <input
            type="date"
            name="end-date"
            v-model="endDate"
            placeholder="END_DATE"
            class="rounded text-white p-1 border focus:ring-3 focus:ring-blue-300 bg-gray-800 border-gray-600 focus:ring-blue-600 ring-offset-gray-800 w-1/6"
        />
        <br>
        <button type="submit" value="Save New Row" class="text-sm mt-2 rounded shadow-md px-2 py-2 bg-gray-400 text-black font-bold hover:bg-gray-700 hover:text-white">
            Save New Row
        </button>
    </form>
</template>

<script>
export default {
    name: 'NewRow',
    data () {
        return {
            uuid: '',
            id: '',
            garageName: '',
            approvalType: '',
            approvalSubType: '',
            startDate: '',
            endDate: ''
        }
    },
    methods: {
        onSubmit (e) {
            e.preventDefault()

            var regex = /^[0-9]+$/

            if(!this.id) {
                alert('AUDATEX_SITE_ID: Make sure to enter a site ID!')
                return
            } else if (!this.id.match(regex)){
                alert('AUDATEX_SITE_ID: Please input a number!')
                return
            } else if (!this.garageName) {
                alert('GARAGE_NAME: Please insert a value!')
                return
            } else if (!this.approvalType) {
                alert('APPROVAL_TYPE: Please insert a value!')
                return
            } else if (!this.startDate) {
                alert('START_DATE: Please insert a value!')
                return
            }

            const newRow = {
                uuid: crypto.randomUUID().replace(/-/g, ""),
                id: parseInt(this.id),
                garageName: this.garageName,
                approvalType: this.approvalType,
                approvalSubType: this.approvalSubType,
                startDate: this.startDate,
                endDate: this.endDate
            }

            this.$emit('submit-new-row', newRow)
        }
    }
}
</script>

