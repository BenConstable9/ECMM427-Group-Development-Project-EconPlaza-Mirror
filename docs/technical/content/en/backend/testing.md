---
title: Testing the API
description: ''
position: 280
category: Backend
---

API Testing is performed using Django's built in Test Manager. The current test coverage is 88%.

To run tests, start up your repository by following the steps in running.md and execute the testing section.

## Testing Structure

accounts.tests.models.test_profile.ProfileCreationTest
<!--Profile has a defined __str__ method.-->
- test_profile_has_str
<!--User and profile correctly reference each other.-->
- test_profile_has_user

accounts.tests.models.test_user.UserCreationTest
<!--User has a defined __str__ method.-->
- test_user_has_str

accounts.tests.models.test_vouch.VouchCreationTest
<!--Check that you can only vouch for a single user once-->
- test_no_duplicate_vouch
<!--Test vouch has appropriate string method-->
- test_string_representation

accounts.tests.permissions.test_user.IsVerifiedTest
<!--Test that a non verified and non admin will fail the check.-->
- test_non_admin_non_verified_user_returns_false
<!--Check we can pass on a safe method.-->
- test_non_admin_non_verified_user_returns_true_on_safe_method
<!--Test that a verified user will pass the permissions test.-->
- test_non_admin_verified_user_returns_true
<!--Check we can pass on a safe method.-->
- test_non_admin_verified_user_returns_true_on_safe_method

accounts.tests.serializers.test_user.UserPostSerializerTest
<!--Test the serialiser returns the expected fields.-->
- test_contains_expected_fields
<!--Test the serialiser returns the expected values.-->
- test_equal_data

accounts.tests.serializers.test_user.UserSerializerTest
<!--Test the serialiser returns the expected fields.-->
- test_contains_expected_fields
<!--Test the serialiser returns the expected values.-->
- test_equal_data

accounts.tests.serializers.test_vouch.VouchSerializerTest
<!--Test the serialiser returns the expected fields.-->
- test_contains_expected_fields
<!--Test the serialiser returns the expected values.-->
- test_equal_data

accounts.tests.views.test_user.AuthenticatedUserViewTest
<!--Test we get a HTTP 200 response when looking at detailed view.-->
- test_get_user
<!--Test we get a HTTP 401 response when looking at the view.-->
- test_get_user_unauth

accounts.tests.viewsets.test_activity.ActivityViewsetTest
<!--Test we get a HTTP 404 response when attempting to delete data.-->
- test_delete_activity
<!--Test we get a HTTP 404 response when attempting to delete data and we aren't authorised.-->
- test_delete_activity_unauth
<!--Test we get a HTTP 200 response when looking at list view.-->
- test_get_activity
<!--Test we get a HTTP 404 response when looking at list view.-->
- test_get_activity_unauth
<!--Test we get a HTTP 405 response when attempting to add data.-->
- test_post_activity
<!--Test we get a HTTP 401 response when attempting to add data as we aren't authorised.-->
- test_post_activity_unauth
<!--Test we get a HTTP 404 response when attempting to update data.-->
- test_put_activity
<!--Test we get a HTTP 404 response when attempting to update data and we aren't authorised.-->
- test_put_activity_unauth

accounts.tests.viewsets.test_memberships.MembershipsViewsetTest
<!--Test we get a HTTP 404 response when attempting to delete data.-->
- test_delete_member
<!--Test we get a HTTP 404 response when attempting to delete data and we aren't authorised.-->
- test_delete_member_unauth
<!--Test we get a HTTP 200 response when looking at list view.-->
- test_get_members
<!--Test we get a HTTP 404 response when looking at list view.-->
- test_get_members_unauth     
<!--Test we get a HTTP 405 response when attempting to add data.-->		
- test_post_member     
<!--Test we get a HTTP 403 response when attempting to add data as we aren't authorised.-->		
- test_post_member_unauth     
<!--Test we get a HTTP 404 response when attempting to update data.-->
- test_put_member  
<!--Test we get a HTTP 404 response when attempting to update data and we aren't authorised.-->   
- test_put_member_unauth     
			
accounts.tests.viewsets.test_user.UserViewsetTest
<!--Test we get a HTTP 405 response when attempting to delete data.-->
- test_delete_user     
<!--Test we get a HTTP 401 response when attempting to delete data and we aren't authorised.-->
- test_delete_user_unauth     
<!--Test we get a HTTP 404 response when looking at the detailed view.-->		
- test_get_invalid_user     		
<!--Test we get a HTTP 200 response when looking at detailed view.-->	
- test_get_user     
<!--Test we get a HTTP 401 response when looking at list view.-->		
- test_get_user_unauth    
<!--Test we get a HTTP 200 response when looking at list view.-->
- test_get_users	
<!--Test we get a HTTP 200 response when looking at list view.-->	
- test_get_users_invalid_search     		
<!--Test we get a HTTP 401 response when looking at detailed view.-->
- test_get_users_unauth     
<!--Test we get a HTTP 200 response when looking at list view.-->			
- test_get_users_valid_search     
<!--Test we get a HTTP 201 response when attempting to register a user-->		
- test_post_user     		
<!--Test we get a HTTP 405 response when attempting to update data.-->
- test_put_user     			
<!--Test we get a HTTP 401 response when attempting to update data and we aren't authorised.-->
- test_put_user_unauth     
			
accounts.tests.viewsets.test_vouch.VouchViewsetTest
- test_delete_vouch     
			<!--Test we get a HTTP 403 response when attempting to delete data.-->
<!--Test we get a HTTP 401 response when attempting to delete data and we aren't authorised.-->
- test_delete_vouch_unauth     
			
<!--Test we get a HTTP 200 response when looking at detailed view.-->
- test_get_vouch     
			
<!--Test we get a HTTP 401 response when looking at detailed view.-->
- test_get_vouch_unauth     
			
<!--Test we get a HTTP 201 response when attempting to add data.-->
- test_post_vouch     
			
<!--Test we get a HTTP 403 response when attempting to add data as we are not authorised.-->
- test_post_vouch_with_unauth     
			
<!--Test we get a HTTP 403 response when attempting to update data.-->
- test_put_vouch     
			
<!--Test we get a HTTP 401 response when attempting to update data and we aren't authorised.-->	
- test_put_vouch_unauth     
			
plazas.tests.models.test_availabletag.AvailableTagCreationTest
<!--Comment has a defined __str__ method.-->
- test_tag_has_str     
			
		
	 
plazas.tests.models.test_comment.CommentCreationTest
<!--Comment has a defined __str__ method.-->
- test_comment_has_str     
			
plazas.tests.models.test_post.PostCreationTest
<!--User has a defined __str__ method.-->
- test_post_has_str     
			
plazas.tests.models.test_tag.TagCreationTest  
<!--Comment has a defined __str__ method.-->
- test_tag_has_str     
			
plazas.tests.serializers.test_availabletag.AvailableTagSerializerTest  
<!--Test the serialiser returns the expected fields.-->
- test_contains_expected_fields     
<!--Test the serialiser returns the expected values.-->		
- test_equal_data     
			
plazas.tests.serializers.test_comment.CommentSerializerTest  
<!--Test the serialiser returns the expected fields.-->
- test_contains_expected_fields   
<!--Test the serialiser returns the expected values.-->  
- test_equal_data     
			
plazas.tests.serializers.test_post.PostSerializerTest   
<!--Test the serialiser returns the expected fields.-->
- test_contains_expected_fields     
<!--Test the serialiser returns the expected values.-->		
- test_equal_data     
 
plazas.tests.serializers.test_tag.TagSerializerTest   
<!--Test the serialiser returns the expected fields.-->
- test_contains_expected_fields     
<!--Test the serialiser returns the expected values.-->	
- test_equal_data     
			
plazas.tests.viewsets.test_availabletag.AvailableTagViewsetTest   
<!--Test we get a HTTP 404 response when attempting to delete data.-->
- test_delete_tag     
<!--Test we get a HTTP 404 response when attempting to delete data and we aren't authorised.-->
- test_delete_tag_unauth     
<!--Test we get a HTTP 200 response when looking at detailed view.-->	
- test_get_tag     
<!--Test we get a HTTP 404 response when looking at detailed view.-->	
- test_get_tag_unauth   
<!--Test we get a HTTP 200 response when looking at list view.-->  
- test_get_tags     
<!--Test we get a HTTP 404 response when looking at list view.-->	
- test_get_tags_unauth     
<!--Test we get a HTTP 403 response when attempting to add data as we aren't authorised.-->
- test_post_member_unauth     
<!--Test we get a HTTP 201 response when attempting to add data.-->		
- test_post_tag     
<!--Test we get a HTTP 400 response when attempting to add data as tags cannot have spaces.-->
- test_post_tag_spaces     
<!--Test we get a HTTP 405 response when attempting to update data.-->		
- test_put_tag     
<!--Test we get a HTTP 401 response when attempting to update data and we aren't authorised.-->
- test_put_tag_unauth     
			
plazas.tests.viewsets.test_comment.CommentViewsetTest  
<!--Test we get a HTTP 405 response when attempting to delete data.--> 
- test_delete_comment     
<!--Test we get a HTTP 401 response when attempting to delete data and we aren't authorised.-->
- test_delete_comment_unauth     
<!--Test we get a HTTP 200 response when looking at detailed view.-->
- test_get_comment     
<!--Test we get the correct comment count when looking at the Plaza view.-->
- test_get_comment_count     
<!--Test we get a HTTP 401 response when looking at detailed view.-->
- test_get_comment_unauth     
<!--Test we get a HTTP 200 response when looking at list view.-->
- test_get_comments     
<!--Test we get a HTTP 401 response when looking at list view.-->
- test_get_comments_unauth     
<!--Test we get a HTTP 201 response when attempting to add data.-->
- test_post_comment     
<!--Test we get a HTTP 403 response when attempting to add data as we aren't verified.-->
- test_post_comment_unverified     
<!--Test we get a HTTP 401 response when attempting to add data as we are not authorised.-->
- test_post_comment_with_unauth     
<!--Test we get a HTTP 405 response when attempting to update data.-->
- test_put_comment     
<!--Test we get a HTTP 401 response when attempting to update data and we aren't authorised.-->	
- test_put_comment_unauth     
			
plazas.tests.viewsets.test_member.MemberViewsetTest   
<!--Test we get a HTTP 404 response when attempting to delete data.-->
- test_delete_member     
<!--Test we get a HTTP 404 response when attempting to delete data and we aren't authorised.-->
- test_delete_member_unauth     
<!--Test we get a HTTP 404 response when looking at list view.-->
- test_get_members     
<!--Test we get a HTTP 404 response when looking at list view.-->
- test_get_members_unauth     
<!--Test we get a HTTP 201 response when attempting to add data.-->
- test_post_member    
<!--Test we get a HTTP 401 response when attempting to add data as we are not authorised.--> 
- test_post_member_duplicate     
<!--Test we get a HTTP 403 response when attempting to add data as we aren't authorised.-->
- test_post_member_unauth     
<!--Test we get a HTTP 404 response when attempting to update data.-->
- test_put_member     
<!--Test we get a HTTP 404 response when attempting to update data and we aren't authorised.-->
- test_put_member_unauth     
			
plazas.tests.viewsets.test_plaza.PlazaViewsetTest   
<!--Test we get the plazas user 1 is a member of first-->
- test_get_my_plazas     
<!--Test that we get plazas ordered by most recent activity-->
- test_get_my_plazas_is_ordered_by_activity     
<!--Test we get the correct list of plazas-->
- test_get_plazas     
<!--Test that we can get popular plazas-->	
- test_get_popular_plazas     
			
plazas.tests.viewsets.test_post.PostViewsetTest   
<!--Test we get a HTTP 405 response when attempting to delete data.-->
- test_delete_post  
<!--Test we get a HTTP 401 response when attempting to delete data and we aren't authorised.-->   
- test_delete_post_unauth     	
<!--Test we get a HTTP 405 response when attempting to delete data.-->
- test_delete_post_without_plaza     
<!--Test we get a HTTP 404 response when looking at the detailed view.-->		
- test_get_invalid_post   
<!--Test we get a HTTP 200 response when looking at detailed view.-->  
- test_get_post     
<!--Test we get a HTTP 401 response when looking at detailed view.-->
- test_get_post_unauth    
<!--Test we get a HTTP 403 response when looking at detailed view.--> 
- test_get_post_unauth_without_plaza   
<!--Test we get a HTTP 403 response when looking at detailed view.-->  
- test_get_post_without_plaza     
<!--Test we get a HTTP 200 response when looking at list view.-->
- test_get_posts     
<!--Test we get a HTTP 401 response when looking at list view.-->
- test_get_posts_unauth     
<!--Test we get a HTTP 401 response when looking at list view.-->
- test_get_posts_unauth_without_plaza     
<!--Test we get a HTTP 200 response when looking at list view.-->
- test_get_posts_without_plaza     
<!--Test we get a HTTP 201 response when attempting to add data.-->
- test_post_post     
<!--Test we get a HTTP 403 response when attempting to add data as we aren't verified.-->
- test_post_post_unverified     
<!--Test we get a HTTP 401 response when attempting to add data as we are not authorised.-->
- test_post_post_with_unauth     
<!--Test we get a HTTP 403 response when attempting to add data as we aren't verified.-->
- test_post_post_without_plaza     
<!--Test the post view count increases-->
- test_post_view     
<!--Test the post view count doesn't increase multiple times for the same ip-->
- test_post_view_no_spam     
<!--Test we get a HTTP 405 response when attempting to update data.-->
- test_put_post   
<!--Test we get a HTTP 401 response when attempting to update data and we aren't authorised.-->  
- test_put_post_unauth     
<!--Test we get a HTTP 401 response when attempting to update data and we aren't authorised.-->
- test_put_post_without_plaza     
