<template>
    <!-- <tr :key="approval.id" v-for="approval in Approvals"> -->
    <ApprovalItem 
        :key="approval.id" v-for="approval in Approvals"
        :Approval="approval" 
        @delete-row="$emit('delete-row', approval.id, approval.approvalType, approval.startDate)"
        @edit-row="$emit('edit-row')"
    />
    <!-- </tr> -->
</template>

<script>
import ApprovalItem from './ApprovalItem'
export default {
    name: 'ApprovalsList',
    components: {
        ApprovalItem
    },
    props: {
        Approvals: Array
    },
    emits: ['delete-row', 'edit-row']
}
</script>