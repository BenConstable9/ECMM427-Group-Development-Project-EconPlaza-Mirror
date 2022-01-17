<template>
    <div>
        <ul
            class="
                w-full
                border
                rounded-r-2xl rounded-b-2xl
                overflow-hidden
                shadow-md
            "
        >
            <vouch-box-header :first-name="firstName" />
            <vouch-box-details :vouches="vouches" />
            <vouch-box-footer :vouches="vouches" />
        </ul>
    </div>
</template>

<script>
import VouchBoxDetails from '~/components/vouch/vouch-box-details'
import VouchBoxHeader from '~/components/vouch/vouch-box-header'
import VouchBoxFooter from '~/components/vouch/vouch-box-footer'

export default {
    name: 'VouchBox',
    components: {
        VouchBoxDetails,
        VouchBoxHeader,
        VouchBoxFooter,
    },
    props: {
        firstName: { type: String, default: null },
        vouches: { type: Array, default: null },
    },
}
</script>

<style></style>
