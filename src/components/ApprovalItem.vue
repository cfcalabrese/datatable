<template>
    <tr class="hover:bg-gray-600 text-right text-sm" @dblclick="editRow">
        <td class='px-2 py-1 ' v-if="!editable" @click="outputRow(Approval)">{{ Approval.AUDATEX_SITE_ID }}</td>
        <td v-else class='tracking-tight overflow-hidden rounded text-right px-2 border border-white  bg-gray-600'>
            <input 
                size="1"
                type="text" 
                v-on:keyup.enter="submitChange"
                v-on:keyup.esc="editRow"
                v-model="editedId"
                class='overflow-hidden rounded text-right focus:outline-none w-auto bg-gray-600 text-bold text-white'
            >
        </td>

        <td class="break-all" v-if="!editable">{{ Approval.GARAGE_NAME }}</td>
        <td v-else class='tracking-tight overflow-hidden rounded border border-white bg-gray-600'>
            <input 
                size="1"
                type="text" 
                v-on:keyup.enter="submitChange" 
                v-on:keyup.esc="editRow"                
                v-model="editedGarageName"
                class='overflow-hidden rounded text-right focus:outline-none w-auto bg-gray-600 text-bold text-white'
            >
        </td>

        <td class="" v-if="!editable">{{ Approval.APPROVAL_TYPE }}</td>
        <td v-else class='tracking-tight overflow-hidden rounded border border-white bg-gray-600'>
            <input 
                size="1"
                type="text" 
                v-on:keyup.enter="submitChange"
                v-on:keyup.esc="editRow"
                v-model="editedApprovalType"
                class='overflow-hidden rounded text-right focus:outline-none w-auto bg-gray-600 text-bold text-white'
            >
        </td>

        <td class="" v-if="!editable">{{ Approval.APPROVAL_SUBTYPE }}</td>
        <td v-else class='tracking-tight overflow-hidden rounded border border-white bg-gray-600'>
            <input 
                size="1"
                type="text" 
                v-on:keyup.enter="submitChange"
                v-on:keyup.esc="editRow"
                v-model="editedApprovalSubType"
                class='overflow-hidden rounded text-right focus:outline-none w-auto bg-gray-600 text-bold text-white'
            >
        </td>

        <td class="" v-if="!editable">{{ Approval.START_DATE }}</td>
        <td v-else class='tracking-tight overflow-hidden rounded border border-white bg-gray-600'>
            <input 
                size="1"
                type="date" 
                v-on:keyup.enter="submitChange"
                v-on:keyup.esc="editRow"
                v-model="editedStartDate"
                class='tracking-[-0.1em] overflow-hidden rounded text-right focus:outline-none w-auto bg-gray-600 text-bold text-white'
            >
        </td>

        <td class="" v-if="!editable">{{ Approval.END_DATE }}</td>
        <td v-else class='tracking-tight overflow-hidden rounded border border-white bg-gray-600'> 
            <input 
                size="1"
                type="date" 
                v-on:keyup.enter="submitChange"
                v-on:keyup.esc="editRow"
                v-model="editedEndDate"
                class='tracking-[-0.1em] overflow-hidden rounded text-right focus:outline-none max-w-1/6 w-auto bg-gray-600 text-bold text-white'
            >
        </td>

        <td :class="editable ? 'py-1 bg-gray-600' : 'py-1 pl-2'">
            <i 
                class="fas fa-pen-to-square text-white cursor-pointer"
                @click="editRow"
            />
        </td>
        <td :class="editable ? 'bg-gray-600 py-1 pr-2' : 'py-1 pr-2'">
            <i 
                class="fas fa-times cursor-pointer text-red-600" 
                @click="$emit('delete-row', Approval.UUID)"
            />
        </td>
    </tr>
</template>

<script>
export default {
    name: 'ApprovalItem',
    props: {
        Approval: Object
    },
    data () {
        return {
            editable: false,
            uuid: this.Approval.UUID,
            editedId: this.Approval.AUDATEX_SITE_ID,
            editedGarageName: this.Approval.GARAGE_NAME,
            editedApprovalType: this.Approval.APPROVAL_TYPE,
            editedApprovalSubType: this.Approval.APPROVAL_SUBTYPE,
            editedStartDate: this.Approval.START_DATE,
            editedEndDate: this.Approval.END_DATE
        }
    },
    methods: {
        editRow () {
            this.editable = !this.editable
        },
        submitChange () {
            const editedRow = {
                uuid: this.uuid,
                id: this.editedId,
                garageName: this.editedGarageName,
                approvalType: this.editedApprovalType,
                approvalSubType: this.editedApprovalSubType,
                startDate: this.editedStartDate,
                endDate: this.editedEndDate
            }

            this.editable = false
            this.$emit('edit-row', editedRow)
        },
        outputRow (row) {
            console.log(row)
        }
    },
    emits: ['delete-row', 'edit-row']
}
</script>
