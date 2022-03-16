<template>
    <tr :class="editable ? 'editable-yes' : ''" @dblclick="editRow">
        <td v-if="!editable" @click="outputRow(Approval)">{{ Approval.id }}</td>
        <td v-else>
            <input 
                type="number" 
                v-on:keyup.enter="submitChange()"
                v-model="editedId"
            >
        </td>

        <td v-if="!editable">{{ Approval.garageName }}</td>
        <td v-else>
            <input 
                type="text" 
                v-on:keyup.enter="submitChange" 
                v-model="editedGarageName"
            >
        </td>

        <td v-if="!editable">{{ Approval.approvalType }}</td>
        <td v-else>
            <input 
                type="text" 
                v-on:keyup.enter="submitChange" 
                v-model="editedApprovalType"
            >
        </td>

        <td v-if="!editable">{{ Approval.approvalSubType }}</td>
        <td v-else>
            <input 
                type="text" 
                v-on:keyup.enter="submitChange" 
                v-model="editedApprovalSubType"
            >
        </td>

        <td v-if="!editable">{{ Approval.startDate }}</td>
        <td v-else>
            <input 
                type="date" 
                v-on:keyup.enter="submitChange" 
                v-model="editedStartDate"
            >
        </td>

        <td v-if="!editable">{{ Approval.endDate }}</td>
        <td v-else> 
            <input 
                type="date" 
                v-on:keyup.enter="submitChange" 
                v-model="editedEndDate"
            >
        </td>

        <td contenteditable="false">
            <i 
                :class="editable ? 'fas fa-pen-to-square edit-on' : 'fas fa-pen-to-square'"
                @click="editRow"
            />
        </td>
        <td contenteditable="false">
            <i 
                class="fas fa-times" 
                @click="$emit('delete-row', Approval.uuid)"
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
            uuid: this.Approval.uuid,
            editedId: this.Approval.id,
            editedGarageName: this.Approval.garageName,
            editedApprovalType: this.Approval.approvalType,
            editedApprovalSubType: this.Approval.approvalSubType,
            editedStartDate: this.Approval.startDate,
            editedEndDate: this.Approval.endDate
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
                startdate: this.editedStartDate,
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

<style>
    .fas.fa-times {
        color: red;
        cursor: pointer;
    }
    .fas.fa-pen-to-square{
        cursor: pointer;
    }
    .fas.fa-pen-to-square.edit-on {
        color: green;
    }
    .editable-yes {
        background: lightgray;
        outline-width: 1px;
        outline-color: darkgrey;
        outline-style:ridge;
    }
</style>