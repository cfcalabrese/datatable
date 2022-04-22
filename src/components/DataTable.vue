<template>
    <div>
        <ApprovalsList />
        <div class="my-2">
            <ButtonItem
                @btn-click="submitChanges"
                text="Submit Changes"
            />
        </div>
    </div>
</template>

<script>
import ApprovalsList from './ApprovalsList'
import ButtonItem from './ButtonItem'

export default {
    name: 'DataTable',
    components:{
        ApprovalsList,
        ButtonItem
    },
    methods: {
        async submitChanges () {
            if (confirm("Are you sure you want to submit these changes?")) {
                const res = await fetch('api/v1/submit', {
                    method: 'POST'
                })

                const data = await res.json()

                window.location.replace("http://localhost:8080")
                
                return data
            }
        }        
    },
}
</script>
