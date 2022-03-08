<template>
    <div id="profile" class="bg-gray-50 rounded-lg border overflow-hidden">
        <div id="profile-header" class="flex flex-col justify-center">
            <div
                id="profile-image"
                class="flex bg-gray-200 justify-center px-5 py-5"
            >
                <div
                    class="w-24 h-24 object-cover rounded-full overflow-hidden"
                >
                    <img src="https://placekitten.com/320/320/" />
                </div>
            </div>
            <div
                id="profile-details"
                class="flex flex-col justify-center px-5 py-5"
            >
                <div class="flex-col">
                    <h1 class="text-lg text-gray-900 font-semibold text-center">
                        {{ user.first_name }} {{ user.last_name }}
                    </h1>
                    <p class="text-gray-700 text-center">
                        @{{ user.username }}
                    </p>
                    <p class="text-sm text-gray-700 text-center">
                        {{ user.email }}
                    </p>
                    <p class="text-md text-gray-700 text-center mt-2">
                        Affiliation: {{ user.institutional_affiliation }}
                    </p>
                    <p class="text-gray-700 text-center mt-2">
                        Member Since:
                        {{
                            new Date(user.date_joined).toLocaleDateString(
                                'en-CA'
                            )
                        }}
                    </p>
                </div>
                <div class="flex items-center space-x-1 justify-center mt-3">
                    <Member v-if="!user.is_staff" />
                    <Staff v-if="user.is_staff" />
                    <Verified v-if="user.verified" />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Member from '~/components/labels/Member'
import Staff from '~/components/labels/staff'
import Verified from '~/components/labels/verified'

export default {
    components: {
        Member,
        Staff,
        Verified,
    },
    props: {
        user: {
            type: Object,
            default: () => {},
        },
    },
}
</script>
