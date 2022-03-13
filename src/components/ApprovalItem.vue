<template>
    <tr :contenteditable="editable" :class="editable ? 'editable-yes' : ''">
        <td>{{ Approval.id }}</td>
        <td>{{ Approval.garageName }}</td>
        <td>{{ Approval.approvalType }}</td>
        <td>{{ Approval.approvalSubType }}</td>
        <td>{{ Approval.startDate }}</td>
        <td>{{ Approval.endDate }}</td>
        <td contenteditable="false">
            <i 
                :class="editable ? 'fas fa-pen-to-square edit-on' : 'fas fa-pen-to-square'"
                @click="editRow"
            />
        </td>
        <td contenteditable="false">
            <i 
                class="fas fa-times" 
                @click="$emit(
                    'delete-row',
                    Approval.id,
                    Approval.approvalType,
                    Approval.startDate
                )"
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
            editable: false
        }
    },
    methods: {
        editRow () {
            this.editable = !this.editable
        } 
    },
    emits: ['delete-row']
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