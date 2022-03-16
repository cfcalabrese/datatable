<template>
    <!-- <tr :key="approval.id" v-for="approval in Approvals"> -->
    <ApprovalItem 
        :key="approval.id" v-for="approval in Approvals"
        :Approval="approval" 
        @delete-row="$emit('delete-row', approval.uuid)"
        @edit-row="submitChange"
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
    methods: {
        submitChange (editedRow) {
            this.$emit('edit-row', editedRow)
        }
    },
    emits: ['delete-row', 'edit-row']
}
</script>