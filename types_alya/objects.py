
from typing import Union, Optional, Any, List
            
from pydantic import BaseModel, ConfigDict
            
reserved_python = ("from_", "format_", "type_")

# pylint: disable=C0301,C0302,W0611

class Update(BaseModel):
    """This [object](https://core.telegram.org/bots/api/#available-types) represents an incoming update.  
At most **one** of the optional parameters can be present in any given update.

    https://core.telegram.org/bots/api/#update
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    update_id: int
    """update_id (int): The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This identifier becomes especially handy if you're using [webhooks](https://core.telegram.org/bots/api/#setwebhook), since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially."""
    message: Optional["Message"] = None
    """message ("Message"): *Optional*. New incoming message of any kind - text, photo, sticker, etc."""
    edited_message: Optional["Message"] = None
    """edited_message ("Message"): *Optional*. New version of a message that is known to the bot and was edited. This update may at times be triggered by changes to message fields that are either unavailable or not actively used by your bot."""
    channel_post: Optional["Message"] = None
    """channel_post ("Message"): *Optional*. New incoming channel post of any kind - text, photo, sticker, etc."""
    edited_channel_post: Optional["Message"] = None
    """edited_channel_post ("Message"): *Optional*. New version of a channel post that is known to the bot and was edited. This update may at times be triggered by changes to message fields that are either unavailable or not actively used by your bot."""
    business_connection: Optional["BusinessConnection"] = None
    """business_connection ("BusinessConnection"): *Optional*. The bot was connected to or disconnected from a business account, or a user edited an existing connection with the bot"""
    business_message: Optional["Message"] = None
    """business_message ("Message"): *Optional*. New message from a connected business account"""
    edited_business_message: Optional["Message"] = None
    """edited_business_message ("Message"): *Optional*. New version of a message from a connected business account"""
    deleted_business_messages: Optional["BusinessMessagesDeleted"] = None
    """deleted_business_messages ("BusinessMessagesDeleted"): *Optional*. Messages were deleted from a connected business account"""
    message_reaction: Optional["MessageReactionUpdated"] = None
    """message_reaction ("MessageReactionUpdated"): *Optional*. A reaction to a message was changed by a user. The bot must be an administrator in the chat and must explicitly specify `'message_reaction'` in the list of *allowed_updates* to receive these updates. The update isn't received for reactions set by bots."""
    message_reaction_count: Optional["MessageReactionCountUpdated"] = None
    """message_reaction_count ("MessageReactionCountUpdated"): *Optional*. Reactions to a message with anonymous reactions were changed. The bot must be an administrator in the chat and must explicitly specify `'message_reaction_count'` in the list of *allowed_updates* to receive these updates. The updates are grouped and can be sent with delay up to a few minutes."""
    inline_query: Optional["InlineQuery"] = None
    """inline_query ("InlineQuery"): *Optional*. New incoming [inline](https://core.telegram.org/bots/api/#inline-mode) query"""
    chosen_inline_result: Optional["ChosenInlineResult"] = None
    """chosen_inline_result ("ChosenInlineResult"): *Optional*. The result of an [inline](https://core.telegram.org/bots/api/#inline-mode) query that was chosen by a user and sent to their chat partner. Please see our documentation on the [feedback collecting](https://core.telegram.org/bots/inline#collecting-feedback) for details on how to enable these updates for your bot."""
    callback_query: Optional["CallbackQuery"] = None
    """callback_query ("CallbackQuery"): *Optional*. New incoming callback query"""
    shipping_query: Optional["ShippingQuery"] = None
    """shipping_query ("ShippingQuery"): *Optional*. New incoming shipping query. Only for invoices with flexible price"""
    pre_checkout_query: Optional["PreCheckoutQuery"] = None
    """pre_checkout_query ("PreCheckoutQuery"): *Optional*. New incoming pre-checkout query. Contains full information about checkout"""
    purchased_paid_media: Optional["PaidMediaPurchased"] = None
    """purchased_paid_media ("PaidMediaPurchased"): *Optional*. A user purchased paid media with a non-empty payload sent by the bot in a non-channel chat"""
    poll: Optional["Poll"] = None
    """poll ("Poll"): *Optional*. New poll state. Bots receive only updates about manually stopped polls and polls, which are sent by the bot"""
    poll_answer: Optional["PollAnswer"] = None
    """poll_answer ("PollAnswer"): *Optional*. A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself."""
    my_chat_member: Optional["ChatMemberUpdated"] = None
    """my_chat_member ("ChatMemberUpdated"): *Optional*. The bot's chat member status was updated in a chat. For private chats, this update is received only when the bot is blocked or unblocked by the user."""
    chat_member: Optional["ChatMemberUpdated"] = None
    """chat_member ("ChatMemberUpdated"): *Optional*. A chat member's status was updated in a chat. The bot must be an administrator in the chat and must explicitly specify `'chat_member'` in the list of *allowed_updates* to receive these updates."""
    chat_join_request: Optional["ChatJoinRequest"] = None
    """chat_join_request ("ChatJoinRequest"): *Optional*. A request to join the chat has been sent. The bot must have the *can_invite_users* administrator right in the chat to receive these updates."""
    chat_boost: Optional["ChatBoostUpdated"] = None
    """chat_boost ("ChatBoostUpdated"): *Optional*. A chat boost was added or changed. The bot must be an administrator in the chat to receive these updates."""
    removed_chat_boost: Optional["ChatBoostRemoved"] = None
    """removed_chat_boost ("ChatBoostRemoved"): *Optional*. A boost was removed from a chat. The bot must be an administrator in the chat to receive these updates."""


class WebhookInfo(BaseModel):
    """Describes the current status of a webhook.

    https://core.telegram.org/bots/api/#webhookinfo
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    url: str
    """url (str): Webhook URL, may be empty if webhook is not set up"""
    has_custom_certificate: bool
    """has_custom_certificate (bool): *True*, if a custom certificate was provided for webhook certificate checks"""
    pending_update_count: int
    """pending_update_count (int): Number of updates awaiting delivery"""
    ip_address: Optional[str] = None
    """ip_address (str): *Optional*. Currently used webhook IP address"""
    last_error_date: Optional[int] = None
    """last_error_date (int): *Optional*. Unix time for the most recent error that happened when trying to deliver an update via webhook"""
    last_error_message: Optional[str] = None
    """last_error_message (str): *Optional*. Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook"""
    last_synchronization_error_date: Optional[int] = None
    """last_synchronization_error_date (int): *Optional*. Unix time of the most recent error that happened when trying to synchronize available updates with Telegram datacenters"""
    max_connections: Optional[int] = None
    """max_connections (int): *Optional*. The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery"""
    allowed_updates: Optional[List[str]] = None
    """allowed_updates (List[str]): *Optional*. A list of update types the bot is subscribed to. Defaults to all update types except *chat_member*"""


class User(BaseModel):
    """This object represents a Telegram user or bot.

    https://core.telegram.org/bots/api/#user
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    id: int
    """id (int): Unique identifier for this user or bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier."""
    is_bot: bool
    """is_bot (bool): *True*, if this user is a bot"""
    first_name: str
    """first_name (str): User's or bot's first name"""
    last_name: Optional[str] = None
    """last_name (str): *Optional*. User's or bot's last name"""
    username: Optional[str] = None
    """username (str): *Optional*. User's or bot's username"""
    language_code: Optional[str] = None
    """language_code (str): *Optional*. [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag) of the user's language"""
    is_premium: Optional[bool] = True
    """is_premium (bool): *Optional*. *True*, if this user is a Telegram Premium user"""
    added_to_attachment_menu: Optional[bool] = True
    """added_to_attachment_menu (bool): *Optional*. *True*, if this user added the bot to the attachment menu"""
    can_join_groups: Optional[bool] = None
    """can_join_groups (bool): *Optional*. *True*, if the bot can be invited to groups. Returned only in [getMe](https://core.telegram.org/bots/api/#getme)."""
    can_read_all_group_messages: Optional[bool] = None
    """can_read_all_group_messages (bool): *Optional*. *True*, if [privacy mode](https://core.telegram.org/bots/features#privacy-mode) is disabled for the bot. Returned only in [getMe](https://core.telegram.org/bots/api/#getme)."""
    supports_inline_queries: Optional[bool] = None
    """supports_inline_queries (bool): *Optional*. *True*, if the bot supports inline queries. Returned only in [getMe](https://core.telegram.org/bots/api/#getme)."""
    can_connect_to_business: Optional[bool] = None
    """can_connect_to_business (bool): *Optional*. *True*, if the bot can be connected to a Telegram Business account to receive its messages. Returned only in [getMe](https://core.telegram.org/bots/api/#getme)."""
    has_main_web_app: Optional[bool] = None
    """has_main_web_app (bool): *Optional*. *True*, if the bot has a main Web App. Returned only in [getMe](https://core.telegram.org/bots/api/#getme)."""


class Chat(BaseModel):
    """This object represents a chat.

    https://core.telegram.org/bots/api/#chat
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    id: int
    """id (int): Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier."""
    type_: str
    """type_ (str): Type of the chat, can be either “private”, “group”, “supergroup” or “channel”"""
    title: Optional[str] = None
    """title (str): *Optional*. Title, for supergroups, channels and group chats"""
    username: Optional[str] = None
    """username (str): *Optional*. Username, for private chats, supergroups and channels if available"""
    first_name: Optional[str] = None
    """first_name (str): *Optional*. First name of the other party in a private chat"""
    last_name: Optional[str] = None
    """last_name (str): *Optional*. Last name of the other party in a private chat"""
    is_forum: Optional[bool] = True
    """is_forum (bool): *Optional*. *True*, if the supergroup chat is a forum (has [topics](https://telegram.org/blog/topics-in-groups-collectible-usernames#topics-in-groups) enabled)"""


class ChatFullInfo(BaseModel):
    """This object contains full information about a chat.

    https://core.telegram.org/bots/api/#chatfullinfo
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    id: int
    """id (int): Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier."""
    type_: str
    """type_ (str): Type of the chat, can be either “private”, “group”, “supergroup” or “channel”"""
    title: Optional[str] = None
    """title (str): *Optional*. Title, for supergroups, channels and group chats"""
    username: Optional[str] = None
    """username (str): *Optional*. Username, for private chats, supergroups and channels if available"""
    first_name: Optional[str] = None
    """first_name (str): *Optional*. First name of the other party in a private chat"""
    last_name: Optional[str] = None
    """last_name (str): *Optional*. Last name of the other party in a private chat"""
    is_forum: Optional[bool] = True
    """is_forum (bool): *Optional*. *True*, if the supergroup chat is a forum (has [topics](https://telegram.org/blog/topics-in-groups-collectible-usernames#topics-in-groups) enabled)"""
    accent_color_id: int
    """accent_color_id (int): Identifier of the accent color for the chat name and backgrounds of the chat photo, reply header, and link preview. See [accent colors](https://core.telegram.org/bots/api/#accent-colors) for more details."""
    max_reaction_count: int
    """max_reaction_count (int): The maximum number of reactions that can be set on a message in the chat"""
    photo: Optional["ChatPhoto"] = None
    """photo ("ChatPhoto"): *Optional*. Chat photo"""
    active_usernames: Optional[List[str]] = None
    """active_usernames (List[str]): *Optional*. If non-empty, the list of all [active chat usernames](https://telegram.org/blog/topics-in-groups-collectible-usernames#collectible-usernames); for private chats, supergroups and channels"""
    birthdate: Optional["Birthdate"] = None
    """birthdate ("Birthdate"): *Optional*. For private chats, the date of birth of the user"""
    business_intro: Optional["BusinessIntro"] = None
    """business_intro ("BusinessIntro"): *Optional*. For private chats with business accounts, the intro of the business"""
    business_location: Optional["BusinessLocation"] = None
    """business_location ("BusinessLocation"): *Optional*. For private chats with business accounts, the location of the business"""
    business_opening_hours: Optional["BusinessOpeningHours"] = None
    """business_opening_hours ("BusinessOpeningHours"): *Optional*. For private chats with business accounts, the opening hours of the business"""
    personal_chat: Optional["Chat"] = None
    """personal_chat ("Chat"): *Optional*. For private chats, the personal channel of the user"""
    available_reactions: Optional[List["ReactionType"]] = None
    """available_reactions (List["ReactionType"]): *Optional*. List of available reactions allowed in the chat. If omitted, then all [emoji reactions](https://core.telegram.org/bots/api/#reactiontypeemoji) are allowed."""
    background_custom_emoji_id: Optional[str] = None
    """background_custom_emoji_id (str): *Optional*. Custom emoji identifier of the emoji chosen by the chat for the reply header and link preview background"""
    profile_accent_color_id: Optional[int] = None
    """profile_accent_color_id (int): *Optional*. Identifier of the accent color for the chat's profile background. See [profile accent colors](https://core.telegram.org/bots/api/#profile-accent-colors) for more details."""
    profile_background_custom_emoji_id: Optional[str] = None
    """profile_background_custom_emoji_id (str): *Optional*. Custom emoji identifier of the emoji chosen by the chat for its profile background"""
    emoji_status_custom_emoji_id: Optional[str] = None
    """emoji_status_custom_emoji_id (str): *Optional*. Custom emoji identifier of the emoji status of the chat or the other party in a private chat"""
    emoji_status_expiration_date: Optional[int] = None
    """emoji_status_expiration_date (int): *Optional*. Expiration date of the emoji status of the chat or the other party in a private chat, in Unix time, if any"""
    bio: Optional[str] = None
    """bio (str): *Optional*. Bio of the other party in a private chat"""
    has_private_forwards: Optional[bool] = True
    """has_private_forwards (bool): *Optional*. *True*, if privacy settings of the other party in the private chat allows to use `tg://user?id=<user_id>` links only in chats with the user"""
    has_restricted_voice_and_video_messages: Optional[bool] = True
    """has_restricted_voice_and_video_messages (bool): *Optional*. *True*, if the privacy settings of the other party restrict sending voice and video note messages in the private chat"""
    join_to_send_messages: Optional[bool] = True
    """join_to_send_messages (bool): *Optional*. *True*, if users need to join the supergroup before they can send messages"""
    join_by_request: Optional[bool] = True
    """join_by_request (bool): *Optional*. *True*, if all users directly joining the supergroup without using an invite link need to be approved by supergroup administrators"""
    description: Optional[str] = None
    """description (str): *Optional*. Description, for groups, supergroups and channel chats"""
    invite_link: Optional[str] = None
    """invite_link (str): *Optional*. Primary invite link, for groups, supergroups and channel chats"""
    pinned_message: Optional["Message"] = None
    """pinned_message ("Message"): *Optional*. The most recent pinned message (by sending date)"""
    permissions: Optional["ChatPermissions"] = None
    """permissions ("ChatPermissions"): *Optional*. Default chat member permissions, for groups and supergroups"""
    can_send_gift: Optional[bool] = True
    """can_send_gift (bool): *Optional*. *True*, if gifts can be sent to the chat"""
    can_send_paid_media: Optional[bool] = True
    """can_send_paid_media (bool): *Optional*. *True*, if paid media messages can be sent or forwarded to the channel chat. The field is available only for channel chats."""
    slow_mode_delay: Optional[int] = None
    """slow_mode_delay (int): *Optional*. For supergroups, the minimum allowed delay between consecutive messages sent by each unprivileged user; in seconds"""
    unrestrict_boost_count: Optional[int] = None
    """unrestrict_boost_count (int): *Optional*. For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions"""
    message_auto_delete_time: Optional[int] = None
    """message_auto_delete_time (int): *Optional*. The time after which all messages sent to the chat will be automatically deleted; in seconds"""
    has_aggressive_anti_spam_enabled: Optional[bool] = True
    """has_aggressive_anti_spam_enabled (bool): *Optional*. *True*, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators."""
    has_hidden_members: Optional[bool] = True
    """has_hidden_members (bool): *Optional*. *True*, if non-administrators can only get the list of bots and administrators in the chat"""
    has_protected_content: Optional[bool] = True
    """has_protected_content (bool): *Optional*. *True*, if messages from the chat can't be forwarded to other chats"""
    has_visible_history: Optional[bool] = True
    """has_visible_history (bool): *Optional*. *True*, if new chat members will have access to old messages; available only to chat administrators"""
    sticker_set_name: Optional[str] = None
    """sticker_set_name (str): *Optional*. For supergroups, name of the group sticker set"""
    can_set_sticker_set: Optional[bool] = True
    """can_set_sticker_set (bool): *Optional*. *True*, if the bot can change the group sticker set"""
    custom_emoji_sticker_set_name: Optional[str] = None
    """custom_emoji_sticker_set_name (str): *Optional*. For supergroups, the name of the group's custom emoji sticker set. Custom emoji from this set can be used by all users and bots in the group."""
    linked_chat_id: Optional[int] = None
    """linked_chat_id (int): *Optional*. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier."""
    location: Optional["ChatLocation"] = None
    """location ("ChatLocation"): *Optional*. For supergroups, the location to which the supergroup is connected"""


class Message(BaseModel):
    """This object represents a message.

    https://core.telegram.org/bots/api/#message
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    message_id: int
    """message_id (int): Unique message identifier inside this chat. In specific instances (e.g., message containing a video sent to a big chat), the server might automatically schedule a message instead of sending it immediately. In such cases, this field will be 0 and the relevant message will be unusable until it is actually sent"""
    message_thread_id: Optional[int] = None
    """message_thread_id (int): *Optional*. Unique identifier of a message thread to which the message belongs; for supergroups only"""
    from_: Optional["User"] = None
    """from_ ("User"): *Optional*. Sender of the message; may be empty for messages sent to channels. For backward compatibility, if the message was sent on behalf of a chat, the field contains a fake sender user in non-channel chats"""
    sender_chat: Optional["Chat"] = None
    """sender_chat ("Chat"): *Optional*. Sender of the message when sent on behalf of a chat. For example, the supergroup itself for messages sent by its anonymous administrators or a linked channel for messages automatically forwarded to the channel's discussion group. For backward compatibility, if the message was sent on behalf of a chat, the field *from* contains a fake sender user in non-channel chats."""
    sender_boost_count: Optional[int] = None
    """sender_boost_count (int): *Optional*. If the sender of the message boosted the chat, the number of boosts added by the user"""
    sender_business_bot: Optional["User"] = None
    """sender_business_bot ("User"): *Optional*. The bot that actually sent the message on behalf of the business account. Available only for outgoing messages sent on behalf of the connected business account."""
    date: int
    """date (int): Date the message was sent in Unix time. It is always a positive number, representing a valid date."""
    business_connection_id: Optional[str] = None
    """business_connection_id (str): *Optional*. Unique identifier of the business connection from which the message was received. If non-empty, the message belongs to a chat of the corresponding business account that is independent from any potential bot chat which might share the same identifier."""
    chat: "Chat"
    """chat ("Chat"): Chat the message belongs to"""
    forward_origin: Optional["MessageOrigin"] = None
    """forward_origin ("MessageOrigin"): *Optional*. Information about the original message for forwarded messages"""
    is_topic_message: Optional[bool] = True
    """is_topic_message (bool): *Optional*. *True*, if the message is sent to a forum topic"""
    is_automatic_forward: Optional[bool] = True
    """is_automatic_forward (bool): *Optional*. *True*, if the message is a channel post that was automatically forwarded to the connected discussion group"""
    reply_to_message: Optional["Message"] = None
    """reply_to_message ("Message"): *Optional*. For replies in the same chat and message thread, the original message. Note that the Message object in this field will not contain further *reply_to_message* fields even if it itself is a reply."""
    external_reply: Optional["ExternalReplyInfo"] = None
    """external_reply ("ExternalReplyInfo"): *Optional*. Information about the message that is being replied to, which may come from another chat or forum topic"""
    quote: Optional["TextQuote"] = None
    """quote ("TextQuote"): *Optional*. For replies that quote part of the original message, the quoted part of the message"""
    reply_to_story: Optional["Story"] = None
    """reply_to_story ("Story"): *Optional*. For replies to a story, the original story"""
    via_bot: Optional["User"] = None
    """via_bot ("User"): *Optional*. Bot through which the message was sent"""
    edit_date: Optional[int] = None
    """edit_date (int): *Optional*. Date the message was last edited in Unix time"""
    has_protected_content: Optional[bool] = True
    """has_protected_content (bool): *Optional*. *True*, if the message can't be forwarded"""
    is_from_offline: Optional[bool] = True
    """is_from_offline (bool): *Optional*. True, if the message was sent by an implicit action, for example, as an away or a greeting business message, or as a scheduled message"""
    media_group_id: Optional[str] = None
    """media_group_id (str): *Optional*. The unique identifier of a media message group this message belongs to"""
    author_signature: Optional[str] = None
    """author_signature (str): *Optional*. Signature of the post author for messages in channels, or the custom title of an anonymous group administrator"""
    text: Optional[str] = None
    """text (str): *Optional*. For text messages, the actual UTF-8 text of the message"""
    entities: Optional[List["MessageEntity"]] = None
    """entities (List["MessageEntity"]): *Optional*. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text"""
    link_preview_options: Optional["LinkPreviewOptions"] = None
    """link_preview_options ("LinkPreviewOptions"): *Optional*. Options used for link preview generation for the message, if it is a text message and link preview options were changed"""
    effect_id: Optional[str] = None
    """effect_id (str): *Optional*. Unique identifier of the message effect added to the message"""
    animation: Optional["Animation"] = None
    """animation ("Animation"): *Optional*. Message is an animation, information about the animation. For backward compatibility, when this field is set, the *document* field will also be set"""
    audio: Optional["Audio"] = None
    """audio ("Audio"): *Optional*. Message is an audio file, information about the file"""
    document: Optional["Document"] = None
    """document ("Document"): *Optional*. Message is a general file, information about the file"""
    paid_media: Optional["PaidMediaInfo"] = None
    """paid_media ("PaidMediaInfo"): *Optional*. Message contains paid media; information about the paid media"""
    photo: Optional[List["PhotoSize"]] = None
    """photo (List["PhotoSize"]): *Optional*. Message is a photo, available sizes of the photo"""
    sticker: Optional["Sticker"] = None
    """sticker ("Sticker"): *Optional*. Message is a sticker, information about the sticker"""
    story: Optional["Story"] = None
    """story ("Story"): *Optional*. Message is a forwarded story"""
    video: Optional["Video"] = None
    """video ("Video"): *Optional*. Message is a video, information about the video"""
    video_note: Optional["VideoNote"] = None
    """video_note ("VideoNote"): *Optional*. Message is a [video note](https://telegram.org/blog/video-messages-and-telescope), information about the video message"""
    voice: Optional["Voice"] = None
    """voice ("Voice"): *Optional*. Message is a voice message, information about the file"""
    caption: Optional[str] = None
    """caption (str): *Optional*. Caption for the animation, audio, document, paid media, photo, video or voice"""
    caption_entities: Optional[List["MessageEntity"]] = None
    """caption_entities (List["MessageEntity"]): *Optional*. For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption"""
    show_caption_above_media: Optional[bool] = True
    """show_caption_above_media (bool): *Optional*. True, if the caption must be shown above the message media"""
    has_media_spoiler: Optional[bool] = True
    """has_media_spoiler (bool): *Optional*. *True*, if the message media is covered by a spoiler animation"""
    contact: Optional["Contact"] = None
    """contact ("Contact"): *Optional*. Message is a shared contact, information about the contact"""
    dice: Optional["Dice"] = None
    """dice ("Dice"): *Optional*. Message is a dice with random value"""
    game: Optional["Game"] = None
    """game ("Game"): *Optional*. Message is a game, information about the game. [More about games »](https://core.telegram.org/bots/api/#games)"""
    poll: Optional["Poll"] = None
    """poll ("Poll"): *Optional*. Message is a native poll, information about the poll"""
    venue: Optional["Venue"] = None
    """venue ("Venue"): *Optional*. Message is a venue, information about the venue. For backward compatibility, when this field is set, the *location* field will also be set"""
    location: Optional["Location"] = None
    """location ("Location"): *Optional*. Message is a shared location, information about the location"""
    new_chat_members: Optional[List["User"]] = None
    """new_chat_members (List["User"]): *Optional*. New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)"""
    left_chat_member: Optional["User"] = None
    """left_chat_member ("User"): *Optional*. A member was removed from the group, information about them (this member may be the bot itself)"""
    new_chat_title: Optional[str] = None
    """new_chat_title (str): *Optional*. A chat title was changed to this value"""
    new_chat_photo: Optional[List["PhotoSize"]] = None
    """new_chat_photo (List["PhotoSize"]): *Optional*. A chat photo was change to this value"""
    delete_chat_photo: Optional[bool] = True
    """delete_chat_photo (bool): *Optional*. Service message: the chat photo was deleted"""
    group_chat_created: Optional[bool] = True
    """group_chat_created (bool): *Optional*. Service message: the group has been created"""
    supergroup_chat_created: Optional[bool] = True
    """supergroup_chat_created (bool): *Optional*. Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup."""
    channel_chat_created: Optional[bool] = True
    """channel_chat_created (bool): *Optional*. Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel."""
    message_auto_delete_timer_changed: Optional["MessageAutoDeleteTimerChanged"] = None
    """message_auto_delete_timer_changed ("MessageAutoDeleteTimerChanged"): *Optional*. Service message: auto-delete timer settings changed in the chat"""
    migrate_to_chat_id: Optional[int] = None
    """migrate_to_chat_id (int): *Optional*. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier."""
    migrate_from_chat_id: Optional[int] = None
    """migrate_from_chat_id (int): *Optional*. The supergroup has been migrated from a group with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier."""
    pinned_message: Optional["MaybeInaccessibleMessage"] = None
    """pinned_message ("MaybeInaccessibleMessage"): *Optional*. Specified message was pinned. Note that the Message object in this field will not contain further *reply_to_message* fields even if it itself is a reply."""
    invoice: Optional["Invoice"] = None
    """invoice ("Invoice"): *Optional*. Message is an invoice for a [payment](https://core.telegram.org/bots/api/#payments), information about the invoice. [More about payments »](https://core.telegram.org/bots/api/#payments)"""
    successful_payment: Optional["SuccessfulPayment"] = None
    """successful_payment ("SuccessfulPayment"): *Optional*. Message is a service message about a successful payment, information about the payment. [More about payments »](https://core.telegram.org/bots/api/#payments)"""
    refunded_payment: Optional["RefundedPayment"] = None
    """refunded_payment ("RefundedPayment"): *Optional*. Message is a service message about a refunded payment, information about the payment. [More about payments »](https://core.telegram.org/bots/api/#payments)"""
    users_shared: Optional["UsersShared"] = None
    """users_shared ("UsersShared"): *Optional*. Service message: users were shared with the bot"""
    chat_shared: Optional["ChatShared"] = None
    """chat_shared ("ChatShared"): *Optional*. Service message: a chat was shared with the bot"""
    connected_website: Optional[str] = None
    """connected_website (str): *Optional*. The domain name of the website on which the user has logged in. [More about Telegram Login »](https://core.telegram.org/widgets/login)"""
    write_access_allowed: Optional["WriteAccessAllowed"] = None
    """write_access_allowed ("WriteAccessAllowed"): *Optional*. Service message: the user allowed the bot to write messages after adding it to the attachment or side menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method [requestWriteAccess](https://core.telegram.org/bots/webapps#initializing-mini-apps)"""
    passport_data: Optional["PassportData"] = None
    """passport_data ("PassportData"): *Optional*. Telegram Passport data"""
    proximity_alert_triggered: Optional["ProximityAlertTriggered"] = None
    """proximity_alert_triggered ("ProximityAlertTriggered"): *Optional*. Service message. A user in the chat triggered another user's proximity alert while sharing Live Location."""
    boost_added: Optional["ChatBoostAdded"] = None
    """boost_added ("ChatBoostAdded"): *Optional*. Service message: user boosted the chat"""
    chat_background_set: Optional["ChatBackground"] = None
    """chat_background_set ("ChatBackground"): *Optional*. Service message: chat background set"""
    forum_topic_created: Optional["ForumTopicCreated"] = None
    """forum_topic_created ("ForumTopicCreated"): *Optional*. Service message: forum topic created"""
    forum_topic_edited: Optional["ForumTopicEdited"] = None
    """forum_topic_edited ("ForumTopicEdited"): *Optional*. Service message: forum topic edited"""
    forum_topic_closed: Optional["ForumTopicClosed"] = None
    """forum_topic_closed ("ForumTopicClosed"): *Optional*. Service message: forum topic closed"""
    forum_topic_reopened: Optional["ForumTopicReopened"] = None
    """forum_topic_reopened ("ForumTopicReopened"): *Optional*. Service message: forum topic reopened"""
    general_forum_topic_hidden: Optional["GeneralForumTopicHidden"] = None
    """general_forum_topic_hidden ("GeneralForumTopicHidden"): *Optional*. Service message: the 'General' forum topic hidden"""
    general_forum_topic_unhidden: Optional["GeneralForumTopicUnhidden"] = None
    """general_forum_topic_unhidden ("GeneralForumTopicUnhidden"): *Optional*. Service message: the 'General' forum topic unhidden"""
    giveaway_created: Optional["GiveawayCreated"] = None
    """giveaway_created ("GiveawayCreated"): *Optional*. Service message: a scheduled giveaway was created"""
    giveaway: Optional["Giveaway"] = None
    """giveaway ("Giveaway"): *Optional*. The message is a scheduled giveaway message"""
    giveaway_winners: Optional["GiveawayWinners"] = None
    """giveaway_winners ("GiveawayWinners"): *Optional*. A giveaway with public winners was completed"""
    giveaway_completed: Optional["GiveawayCompleted"] = None
    """giveaway_completed ("GiveawayCompleted"): *Optional*. Service message: a giveaway without public winners was completed"""
    video_chat_scheduled: Optional["VideoChatScheduled"] = None
    """video_chat_scheduled ("VideoChatScheduled"): *Optional*. Service message: video chat scheduled"""
    video_chat_started: Optional["VideoChatStarted"] = None
    """video_chat_started ("VideoChatStarted"): *Optional*. Service message: video chat started"""
    video_chat_ended: Optional["VideoChatEnded"] = None
    """video_chat_ended ("VideoChatEnded"): *Optional*. Service message: video chat ended"""
    video_chat_participants_invited: Optional["VideoChatParticipantsInvited"] = None
    """video_chat_participants_invited ("VideoChatParticipantsInvited"): *Optional*. Service message: new participants invited to a video chat"""
    web_app_data: Optional["WebAppData"] = None
    """web_app_data ("WebAppData"): *Optional*. Service message: data sent by a Web App"""
    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """reply_markup ("InlineKeyboardMarkup"): *Optional*. Inline keyboard attached to the message. `login_url` buttons are represented as ordinary `url` buttons."""


class MessageId(BaseModel):
    """This object represents a unique message identifier.

    https://core.telegram.org/bots/api/#messageid
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    message_id: int
    """message_id (int): Unique message identifier. In specific instances (e.g., message containing a video sent to a big chat), the server might automatically schedule a message instead of sending it immediately. In such cases, this field will be 0 and the relevant message will be unusable until it is actually sent"""


class InaccessibleMessage(BaseModel):
    """This object describes a message that was deleted or is otherwise inaccessible to the bot.

    https://core.telegram.org/bots/api/#inaccessiblemessage
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    chat: "Chat"
    """chat ("Chat"): Chat the message belonged to"""
    message_id: int
    """message_id (int): Unique message identifier inside the chat"""
    date: int
    """date (int): Always 0. The field can be used to differentiate regular and inaccessible messages."""


MaybeInaccessibleMessage = Union["Message", "InaccessibleMessage"]
"""This object describes a message that can be inaccessible to the bot. It can be one of

* [Message](https://core.telegram.org/bots/api/#message)
* [InaccessibleMessage](https://core.telegram.org/bots/api/#inaccessiblemessage)"""


class MessageEntity(BaseModel):
    """This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.

    https://core.telegram.org/bots/api/#messageentity
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str
    """type_ (str): Type of the entity. Currently, can be “mention” (`@username`), “hashtag” (`#hashtag` or `#hashtag@chatusername`), “cashtag” (`$USD` or `$USD@chatusername`), “bot_command” (`/start@jobs_bot`), “url” (`https://telegram.org`), “email” (`do-not-reply@telegram.org`), “phone_number” (`+1-212-555-0123`), “bold” (**bold text**), “italic” (*italic text*), “underline” (underlined text), “strikethrough” (strikethrough text), “spoiler” (spoiler message), “blockquote” (block quotation), “expandable_blockquote” (collapsed-by-default block quotation), “code” (monowidth string), “pre” (monowidth block), “text_link” (for clickable text URLs), “text_mention” (for users [without usernames](https://telegram.org/blog/edit#new-mentions)), “custom_emoji” (for inline custom emoji stickers)"""
    offset: int
    """offset (int): Offset in [UTF-16 code units](https://core.telegram.org/api/entities#entity-length) to the start of the entity"""
    length: int
    """length (int): Length of the entity in [UTF-16 code units](https://core.telegram.org/api/entities#entity-length)"""
    url: Optional[str] = None
    """url (str): *Optional*. For “text_link” only, URL that will be opened after user taps on the text"""
    user: Optional["User"] = None
    """user ("User"): *Optional*. For “text_mention” only, the mentioned user"""
    language: Optional[str] = None
    """language (str): *Optional*. For “pre” only, the programming language of the entity text"""
    custom_emoji_id: Optional[str] = None
    """custom_emoji_id (str): *Optional*. For “custom_emoji” only, unique identifier of the custom emoji. Use [getCustomEmojiStickers](https://core.telegram.org/bots/api/#getcustomemojistickers) to get full information about the sticker"""


class TextQuote(BaseModel):
    """This object contains information about the quoted part of a message that is replied to by the given message.

    https://core.telegram.org/bots/api/#textquote
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    text: str
    """text (str): Text of the quoted part of a message that is replied to by the given message"""
    entities: Optional[List["MessageEntity"]] = None
    """entities (List["MessageEntity"]): *Optional*. Special entities that appear in the quote. Currently, only *bold*, *italic*, *underline*, *strikethrough*, *spoiler*, and *custom_emoji* entities are kept in quotes."""
    position: int
    """position (int): Approximate quote position in the original message in UTF-16 code units as specified by the sender"""
    is_manual: Optional[bool] = True
    """is_manual (bool): *Optional*. True, if the quote was chosen manually by the message sender. Otherwise, the quote was added automatically by the server."""


class ExternalReplyInfo(BaseModel):
    """This object contains information about a message that is being replied to, which may come from another chat or forum topic.

    https://core.telegram.org/bots/api/#externalreplyinfo
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    origin: "MessageOrigin"
    """origin ("MessageOrigin"): Origin of the message replied to by the given message"""
    chat: Optional["Chat"] = None
    """chat ("Chat"): *Optional*. Chat the original message belongs to. Available only if the chat is a supergroup or a channel."""
    message_id: Optional[int] = None
    """message_id (int): *Optional*. Unique message identifier inside the original chat. Available only if the original chat is a supergroup or a channel."""
    link_preview_options: Optional["LinkPreviewOptions"] = None
    """link_preview_options ("LinkPreviewOptions"): *Optional*. Options used for link preview generation for the original message, if it is a text message"""
    animation: Optional["Animation"] = None
    """animation ("Animation"): *Optional*. Message is an animation, information about the animation"""
    audio: Optional["Audio"] = None
    """audio ("Audio"): *Optional*. Message is an audio file, information about the file"""
    document: Optional["Document"] = None
    """document ("Document"): *Optional*. Message is a general file, information about the file"""
    paid_media: Optional["PaidMediaInfo"] = None
    """paid_media ("PaidMediaInfo"): *Optional*. Message contains paid media; information about the paid media"""
    photo: Optional[List["PhotoSize"]] = None
    """photo (List["PhotoSize"]): *Optional*. Message is a photo, available sizes of the photo"""
    sticker: Optional["Sticker"] = None
    """sticker ("Sticker"): *Optional*. Message is a sticker, information about the sticker"""
    story: Optional["Story"] = None
    """story ("Story"): *Optional*. Message is a forwarded story"""
    video: Optional["Video"] = None
    """video ("Video"): *Optional*. Message is a video, information about the video"""
    video_note: Optional["VideoNote"] = None
    """video_note ("VideoNote"): *Optional*. Message is a [video note](https://telegram.org/blog/video-messages-and-telescope), information about the video message"""
    voice: Optional["Voice"] = None
    """voice ("Voice"): *Optional*. Message is a voice message, information about the file"""
    has_media_spoiler: Optional[bool] = True
    """has_media_spoiler (bool): *Optional*. *True*, if the message media is covered by a spoiler animation"""
    contact: Optional["Contact"] = None
    """contact ("Contact"): *Optional*. Message is a shared contact, information about the contact"""
    dice: Optional["Dice"] = None
    """dice ("Dice"): *Optional*. Message is a dice with random value"""
    game: Optional["Game"] = None
    """game ("Game"): *Optional*. Message is a game, information about the game. [More about games »](https://core.telegram.org/bots/api/#games)"""
    giveaway: Optional["Giveaway"] = None
    """giveaway ("Giveaway"): *Optional*. Message is a scheduled giveaway, information about the giveaway"""
    giveaway_winners: Optional["GiveawayWinners"] = None
    """giveaway_winners ("GiveawayWinners"): *Optional*. A giveaway with public winners was completed"""
    invoice: Optional["Invoice"] = None
    """invoice ("Invoice"): *Optional*. Message is an invoice for a [payment](https://core.telegram.org/bots/api/#payments), information about the invoice. [More about payments »](https://core.telegram.org/bots/api/#payments)"""
    location: Optional["Location"] = None
    """location ("Location"): *Optional*. Message is a shared location, information about the location"""
    poll: Optional["Poll"] = None
    """poll ("Poll"): *Optional*. Message is a native poll, information about the poll"""
    venue: Optional["Venue"] = None
    """venue ("Venue"): *Optional*. Message is a venue, information about the venue"""


class ReplyParameters(BaseModel):
    """Describes reply parameters for the message that is being sent.

    https://core.telegram.org/bots/api/#replyparameters
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    message_id: int
    """message_id (int): Identifier of the message that will be replied to in the current chat, or in the chat *chat_id* if it is specified"""
    chat_id: Optional[Union[int, str]] = None
    """chat_id (Union[int, str]): *Optional*. If the message to be replied to is from a different chat, unique identifier for the chat or username of the channel (in the format `@channelusername`). Not supported for messages sent on behalf of a business account."""
    allow_sending_without_reply: Optional[bool] = None
    """allow_sending_without_reply (bool): *Optional*. Pass *True* if the message should be sent even if the specified message to be replied to is not found. Always *False* for replies in another chat or forum topic. Always *True* for messages sent on behalf of a business account."""
    quote: Optional[str] = None
    """quote (str): *Optional*. Quoted part of the message to be replied to; 0-1024 characters after entities parsing. The quote must be an exact substring of the message to be replied to, including *bold*, *italic*, *underline*, *strikethrough*, *spoiler*, and *custom_emoji* entities. The message will fail to send if the quote isn't found in the original message."""
    quote_parse_mode: Optional[str] = None
    """quote_parse_mode (str): *Optional*. Mode for parsing entities in the quote. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details."""
    quote_entities: Optional[List["MessageEntity"]] = None
    """quote_entities (List["MessageEntity"]): *Optional*. A JSON-serialized list of special entities that appear in the quote. It can be specified instead of *quote_parse_mode*."""
    quote_position: Optional[int] = None
    """quote_position (int): *Optional*. Position of the quote in the original message in UTF-16 code units"""


MessageOrigin = Union["MessageOriginUser", "MessageOriginHiddenUser",
                      "MessageOriginChat", "MessageOriginChannel"]
"""This object describes the origin of a message. It can be one of

* [MessageOriginUser](https://core.telegram.org/bots/api/#messageoriginuser)
* [MessageOriginHiddenUser](https://core.telegram.org/bots/api/#messageoriginhiddenuser)
* [MessageOriginChat](https://core.telegram.org/bots/api/#messageoriginchat)
* [MessageOriginChannel](https://core.telegram.org/bots/api/#messageoriginchannel)"""


class MessageOriginUser(BaseModel):
    """The message was originally sent by a known user.

    https://core.telegram.org/bots/api/#messageoriginuser
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "user"
    """type_ (str): Type of the message origin, always “user”"""
    date: int
    """date (int): Date the message was sent originally in Unix time"""
    sender_user: "User"
    """sender_user ("User"): User that sent the message originally"""


class MessageOriginHiddenUser(BaseModel):
    """The message was originally sent by an unknown user.

    https://core.telegram.org/bots/api/#messageoriginhiddenuser
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "hidden_user"
    """type_ (str): Type of the message origin, always “hidden_user”"""
    date: int
    """date (int): Date the message was sent originally in Unix time"""
    sender_user_name: str
    """sender_user_name (str): Name of the user that sent the message originally"""


class MessageOriginChat(BaseModel):
    """The message was originally sent on behalf of a chat to a group chat.

    https://core.telegram.org/bots/api/#messageoriginchat
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "chat"
    """type_ (str): Type of the message origin, always “chat”"""
    date: int
    """date (int): Date the message was sent originally in Unix time"""
    sender_chat: "Chat"
    """sender_chat ("Chat"): Chat that sent the message originally"""
    author_signature: Optional[str] = None
    """author_signature (str): *Optional*. For messages originally sent by an anonymous chat administrator, original message author signature"""


class MessageOriginChannel(BaseModel):
    """The message was originally sent to a channel chat.

    https://core.telegram.org/bots/api/#messageoriginchannel
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "channel"
    """type_ (str): Type of the message origin, always “channel”"""
    date: int
    """date (int): Date the message was sent originally in Unix time"""
    chat: "Chat"
    """chat ("Chat"): Channel chat to which the message was originally sent"""
    message_id: int
    """message_id (int): Unique message identifier inside the chat"""
    author_signature: Optional[str] = None
    """author_signature (str): *Optional*. Signature of the original post author"""


class PhotoSize(BaseModel):
    """This object represents one size of a photo or a [file](https://core.telegram.org/bots/api/#document) / [sticker](https://core.telegram.org/bots/api/#sticker) thumbnail.

    https://core.telegram.org/bots/api/#photosize
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    file_id: str
    """file_id (str): Identifier for this file, which can be used to download or reuse the file"""
    file_unique_id: str
    """file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file."""
    width: int
    """width (int): Photo width"""
    height: int
    """height (int): Photo height"""
    file_size: Optional[int] = None
    """file_size (int): *Optional*. File size in bytes"""


class Animation(BaseModel):
    """This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).

    https://core.telegram.org/bots/api/#animation
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    file_id: str
    """file_id (str): Identifier for this file, which can be used to download or reuse the file"""
    file_unique_id: str
    """file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file."""
    width: int
    """width (int): Video width as defined by the sender"""
    height: int
    """height (int): Video height as defined by the sender"""
    duration: int
    """duration (int): Duration of the video in seconds as defined by the sender"""
    thumbnail: Optional["PhotoSize"] = None
    """thumbnail ("PhotoSize"): *Optional*. Animation thumbnail as defined by the sender"""
    file_name: Optional[str] = None
    """file_name (str): *Optional*. Original animation filename as defined by the sender"""
    mime_type: Optional[str] = None
    """mime_type (str): *Optional*. MIME type of the file as defined by the sender"""
    file_size: Optional[int] = None
    """file_size (int): *Optional*. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value."""


class Audio(BaseModel):
    """This object represents an audio file to be treated as music by the Telegram clients.

    https://core.telegram.org/bots/api/#audio
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    file_id: str
    """file_id (str): Identifier for this file, which can be used to download or reuse the file"""
    file_unique_id: str
    """file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file."""
    duration: int
    """duration (int): Duration of the audio in seconds as defined by the sender"""
    performer: Optional[str] = None
    """performer (str): *Optional*. Performer of the audio as defined by the sender or by audio tags"""
    title: Optional[str] = None
    """title (str): *Optional*. Title of the audio as defined by the sender or by audio tags"""
    file_name: Optional[str] = None
    """file_name (str): *Optional*. Original filename as defined by the sender"""
    mime_type: Optional[str] = None
    """mime_type (str): *Optional*. MIME type of the file as defined by the sender"""
    file_size: Optional[int] = None
    """file_size (int): *Optional*. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value."""
    thumbnail: Optional["PhotoSize"] = None
    """thumbnail ("PhotoSize"): *Optional*. Thumbnail of the album cover to which the music file belongs"""


class Document(BaseModel):
    """This object represents a general file (as opposed to [photos](https://core.telegram.org/bots/api/#photosize), [voice messages](https://core.telegram.org/bots/api/#voice) and [audio files](https://core.telegram.org/bots/api/#audio)).

    https://core.telegram.org/bots/api/#document
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    file_id: str
    """file_id (str): Identifier for this file, which can be used to download or reuse the file"""
    file_unique_id: str
    """file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file."""
    thumbnail: Optional["PhotoSize"] = None
    """thumbnail ("PhotoSize"): *Optional*. Document thumbnail as defined by the sender"""
    file_name: Optional[str] = None
    """file_name (str): *Optional*. Original filename as defined by the sender"""
    mime_type: Optional[str] = None
    """mime_type (str): *Optional*. MIME type of the file as defined by the sender"""
    file_size: Optional[int] = None
    """file_size (int): *Optional*. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value."""


class Story(BaseModel):
    """This object represents a story.

    https://core.telegram.org/bots/api/#story
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    chat: "Chat"
    """chat ("Chat"): Chat that posted the story"""
    id: int
    """id (int): Unique identifier for the story in the chat"""


class Video(BaseModel):
    """This object represents a video file.

    https://core.telegram.org/bots/api/#video
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    file_id: str
    """file_id (str): Identifier for this file, which can be used to download or reuse the file"""
    file_unique_id: str
    """file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file."""
    width: int
    """width (int): Video width as defined by the sender"""
    height: int
    """height (int): Video height as defined by the sender"""
    duration: int
    """duration (int): Duration of the video in seconds as defined by the sender"""
    thumbnail: Optional["PhotoSize"] = None
    """thumbnail ("PhotoSize"): *Optional*. Video thumbnail"""
    cover: Optional[List["PhotoSize"]] = None
    """cover (List["PhotoSize"]): *Optional*. Available sizes of the cover of the video in the message"""
    start_timestamp: Optional[int] = None
    """start_timestamp (int): *Optional*. Timestamp in seconds from which the video will play in the message"""
    file_name: Optional[str] = None
    """file_name (str): *Optional*. Original filename as defined by the sender"""
    mime_type: Optional[str] = None
    """mime_type (str): *Optional*. MIME type of the file as defined by the sender"""
    file_size: Optional[int] = None
    """file_size (int): *Optional*. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value."""


class VideoNote(BaseModel):
    """This object represents a [video message](https://telegram.org/blog/video-messages-and-telescope) (available in Telegram apps as of [v.4.0](https://telegram.org/blog/video-messages-and-telescope)).

    https://core.telegram.org/bots/api/#videonote
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    file_id: str
    """file_id (str): Identifier for this file, which can be used to download or reuse the file"""
    file_unique_id: str
    """file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file."""
    length: int
    """length (int): Video width and height (diameter of the video message) as defined by the sender"""
    duration: int
    """duration (int): Duration of the video in seconds as defined by the sender"""
    thumbnail: Optional["PhotoSize"] = None
    """thumbnail ("PhotoSize"): *Optional*. Video thumbnail"""
    file_size: Optional[int] = None
    """file_size (int): *Optional*. File size in bytes"""


class Voice(BaseModel):
    """This object represents a voice note.

    https://core.telegram.org/bots/api/#voice
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    file_id: str
    """file_id (str): Identifier for this file, which can be used to download or reuse the file"""
    file_unique_id: str
    """file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file."""
    duration: int
    """duration (int): Duration of the audio in seconds as defined by the sender"""
    mime_type: Optional[str] = None
    """mime_type (str): *Optional*. MIME type of the file as defined by the sender"""
    file_size: Optional[int] = None
    """file_size (int): *Optional*. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value."""


class PaidMediaInfo(BaseModel):
    """Describes the paid media added to a message.

    https://core.telegram.org/bots/api/#paidmediainfo
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    star_count: int
    """star_count (int): The number of Telegram Stars that must be paid to buy access to the media"""
    paid_media: List["PaidMedia"]
    """paid_media (List["PaidMedia"]): Information about the paid media"""


PaidMedia = Union["PaidMediaPreview", "PaidMediaPhoto", "PaidMediaVideo"]
"""This object describes paid media. Currently, it can be one of

* [PaidMediaPreview](https://core.telegram.org/bots/api/#paidmediapreview)
* [PaidMediaPhoto](https://core.telegram.org/bots/api/#paidmediaphoto)
* [PaidMediaVideo](https://core.telegram.org/bots/api/#paidmediavideo)"""


class PaidMediaPreview(BaseModel):
    """The paid media isn't available before the payment.

    https://core.telegram.org/bots/api/#paidmediapreview
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "preview"
    """type_ (str): Type of the paid media, always “preview”"""
    width: Optional[int] = None
    """width (int): *Optional*. Media width as defined by the sender"""
    height: Optional[int] = None
    """height (int): *Optional*. Media height as defined by the sender"""
    duration: Optional[int] = None
    """duration (int): *Optional*. Duration of the media in seconds as defined by the sender"""


class PaidMediaPhoto(BaseModel):
    """The paid media is a photo.

    https://core.telegram.org/bots/api/#paidmediaphoto
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "photo"
    """type_ (str): Type of the paid media, always “photo”"""
    photo: List["PhotoSize"]
    """photo (List["PhotoSize"]): The photo"""


class PaidMediaVideo(BaseModel):
    """The paid media is a video.

    https://core.telegram.org/bots/api/#paidmediavideo
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "video"
    """type_ (str): Type of the paid media, always “video”"""
    video: "Video"
    """video ("Video"): The video"""


class Contact(BaseModel):
    """This object represents a phone contact.

    https://core.telegram.org/bots/api/#contact
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    phone_number: str
    """phone_number (str): Contact's phone number"""
    first_name: str
    """first_name (str): Contact's first name"""
    last_name: Optional[str] = None
    """last_name (str): *Optional*. Contact's last name"""
    user_id: Optional[int] = None
    """user_id (int): *Optional*. Contact's user identifier in Telegram. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier."""
    vcard: Optional[str] = None
    """vcard (str): *Optional*. Additional data about the contact in the form of a [vCard](https://en.wikipedia.org/wiki/VCard)"""


class Dice(BaseModel):
    """This object represents an animated emoji that displays a random value.

    https://core.telegram.org/bots/api/#dice
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    emoji: str
    """emoji (str): Emoji on which the dice throw animation is based"""
    value: int
    """value (int): Value of the dice, 1-6 for “🎲”, “🎯” and “🎳” base emoji, 1-5 for “🏀” and “⚽” base emoji, 1-64 for “🎰” base emoji"""


class PollOption(BaseModel):
    """This object contains information about one answer option in a poll.

    https://core.telegram.org/bots/api/#polloption
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    text: str
    """text (str): Option text, 1-100 characters"""
    text_entities: Optional[List["MessageEntity"]] = None
    """text_entities (List["MessageEntity"]): *Optional*. Special entities that appear in the option *text*. Currently, only custom emoji entities are allowed in poll option texts"""
    voter_count: int
    """voter_count (int): Number of users that voted for this option"""


class InputPollOption(BaseModel):
    """This object contains information about one answer option in a poll to be sent.

    https://core.telegram.org/bots/api/#inputpolloption
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    text: str
    """text (str): Option text, 1-100 characters"""
    text_parse_mode: Optional[str] = None
    """text_parse_mode (str): *Optional*. Mode for parsing entities in the text. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. Currently, only custom emoji entities are allowed"""
    text_entities: Optional[List["MessageEntity"]] = None
    """text_entities (List["MessageEntity"]): *Optional*. A JSON-serialized list of special entities that appear in the poll option text. It can be specified instead of *text_parse_mode*"""


class PollAnswer(BaseModel):
    """This object represents an answer of a user in a non-anonymous poll.

    https://core.telegram.org/bots/api/#pollanswer
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    poll_id: str
    """poll_id (str): Unique poll identifier"""
    voter_chat: Optional["Chat"] = None
    """voter_chat ("Chat"): *Optional*. The chat that changed the answer to the poll, if the voter is anonymous"""
    user: Optional["User"] = None
    """user ("User"): *Optional*. The user that changed the answer to the poll, if the voter isn't anonymous"""
    option_ids: List[int]
    """option_ids (List[int]): 0-based identifiers of chosen answer options. May be empty if the vote was retracted."""


class Poll(BaseModel):
    """This object contains information about a poll.

    https://core.telegram.org/bots/api/#poll
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    id: str
    """id (str): Unique poll identifier"""
    question: str
    """question (str): Poll question, 1-300 characters"""
    question_entities: Optional[List["MessageEntity"]] = None
    """question_entities (List["MessageEntity"]): *Optional*. Special entities that appear in the *question*. Currently, only custom emoji entities are allowed in poll questions"""
    options: List["PollOption"]
    """options (List["PollOption"]): List of poll options"""
    total_voter_count: int
    """total_voter_count (int): Total number of users that voted in the poll"""
    is_closed: bool
    """is_closed (bool): *True*, if the poll is closed"""
    is_anonymous: bool
    """is_anonymous (bool): *True*, if the poll is anonymous"""
    type_: str
    """type_ (str): Poll type, currently can be “regular” or “quiz”"""
    allows_multiple_answers: bool
    """allows_multiple_answers (bool): *True*, if the poll allows multiple answers"""
    correct_option_id: Optional[int] = None
    """correct_option_id (int): *Optional*. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot."""
    explanation: Optional[str] = None
    """explanation (str): *Optional*. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters"""
    explanation_entities: Optional[List["MessageEntity"]] = None
    """explanation_entities (List["MessageEntity"]): *Optional*. Special entities like usernames, URLs, bot commands, etc. that appear in the *explanation*"""
    open_period: Optional[int] = None
    """open_period (int): *Optional*. Amount of time in seconds the poll will be active after creation"""
    close_date: Optional[int] = None
    """close_date (int): *Optional*. Point in time (Unix timestamp) when the poll will be automatically closed"""


class Location(BaseModel):
    """This object represents a point on the map.

    https://core.telegram.org/bots/api/#location
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    latitude: float
    """latitude (float): Latitude as defined by the sender"""
    longitude: float
    """longitude (float): Longitude as defined by the sender"""
    horizontal_accuracy: Optional[float] = None
    """horizontal_accuracy (float): *Optional*. The radius of uncertainty for the location, measured in meters; 0-1500"""
    live_period: Optional[int] = None
    """live_period (int): *Optional*. Time relative to the message sending date, during which the location can be updated; in seconds. For active live locations only."""
    heading: Optional[int] = None
    """heading (int): *Optional*. The direction in which user is moving, in degrees; 1-360. For active live locations only."""
    proximity_alert_radius: Optional[int] = None
    """proximity_alert_radius (int): *Optional*. The maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only."""


class Venue(BaseModel):
    """This object represents a venue.

    https://core.telegram.org/bots/api/#venue
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    location: "Location"
    """location ("Location"): Venue location. Can't be a live location"""
    title: str
    """title (str): Name of the venue"""
    address: str
    """address (str): Address of the venue"""
    foursquare_id: Optional[str] = None
    """foursquare_id (str): *Optional*. Foursquare identifier of the venue"""
    foursquare_type: Optional[str] = None
    """foursquare_type (str): *Optional*. Foursquare type of the venue. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)"""
    google_place_id: Optional[str] = None
    """google_place_id (str): *Optional*. Google Places identifier of the venue"""
    google_place_type: Optional[str] = None
    """google_place_type (str): *Optional*. Google Places type of the venue. (See [supported types](https://developers.google.com/places/web-service/supported_types).)"""


class WebAppData(BaseModel):
    """Describes data sent from a [Web App](https://core.telegram.org/bots/webapps) to the bot.

    https://core.telegram.org/bots/api/#webappdata
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    data: str
    """data (str): The data. Be aware that a bad client can send arbitrary data in this field."""
    button_text: str
    """button_text (str): Text of the *web_app* keyboard button from which the Web App was opened. Be aware that a bad client can send arbitrary data in this field."""


class ProximityAlertTriggered(BaseModel):
    """This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.

    https://core.telegram.org/bots/api/#proximityalerttriggered
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    traveler: "User"
    """traveler ("User"): User that triggered the alert"""
    watcher: "User"
    """watcher ("User"): User that set the alert"""
    distance: int
    """distance (int): The distance between the users"""


class MessageAutoDeleteTimerChanged(BaseModel):
    """This object represents a service message about a change in auto-delete timer settings.

    https://core.telegram.org/bots/api/#messageautodeletetimerchanged
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    message_auto_delete_time: int
    """message_auto_delete_time (int): New auto-delete time for messages in the chat; in seconds"""


class ChatBoostAdded(BaseModel):
    """This object represents a service message about a user boosting a chat.

    https://core.telegram.org/bots/api/#chatboostadded
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    boost_count: int
    """boost_count (int): Number of boosts added by the user"""


BackgroundFill = Union["BackgroundFillSolid",
                       "BackgroundFillGradient", "BackgroundFillFreeformGradient"]
"""This object describes the way a background is filled based on the selected colors. Currently, it can be one of

* [BackgroundFillSolid](https://core.telegram.org/bots/api/#backgroundfillsolid)
* [BackgroundFillGradient](https://core.telegram.org/bots/api/#backgroundfillgradient)
* [BackgroundFillFreeformGradient](https://core.telegram.org/bots/api/#backgroundfillfreeformgradient)"""


class BackgroundFillSolid(BaseModel):
    """The background is filled using the selected color.

    https://core.telegram.org/bots/api/#backgroundfillsolid
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "solid"
    """type_ (str): Type of the background fill, always “solid”"""
    color: int
    """color (int): The color of the background fill in the RGB24 format"""


class BackgroundFillGradient(BaseModel):
    """The background is a gradient fill.

    https://core.telegram.org/bots/api/#backgroundfillgradient
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "gradient"
    """type_ (str): Type of the background fill, always “gradient”"""
    top_color: int
    """top_color (int): Top color of the gradient in the RGB24 format"""
    bottom_color: int
    """bottom_color (int): Bottom color of the gradient in the RGB24 format"""
    rotation_angle: int
    """rotation_angle (int): Clockwise rotation angle of the background fill in degrees; 0-359"""


class BackgroundFillFreeformGradient(BaseModel):
    """The background is a freeform gradient that rotates after every message in the chat.

    https://core.telegram.org/bots/api/#backgroundfillfreeformgradient
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "freeform_gradient"
    """type_ (str): Type of the background fill, always “freeform_gradient”"""
    colors: List[int]
    """colors (List[int]): A list of the 3 or 4 base colors that are used to generate the freeform gradient in the RGB24 format"""


BackgroundType = Union["BackgroundTypeFill", "BackgroundTypeWallpaper",
                       "BackgroundTypePattern", "BackgroundTypeChatTheme"]
"""This object describes the type of a background. Currently, it can be one of

* [BackgroundTypeFill](https://core.telegram.org/bots/api/#backgroundtypefill)
* [BackgroundTypeWallpaper](https://core.telegram.org/bots/api/#backgroundtypewallpaper)
* [BackgroundTypePattern](https://core.telegram.org/bots/api/#backgroundtypepattern)
* [BackgroundTypeChatTheme](https://core.telegram.org/bots/api/#backgroundtypechattheme)"""


class BackgroundTypeFill(BaseModel):
    """The background is automatically filled based on the selected colors.

    https://core.telegram.org/bots/api/#backgroundtypefill
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "fill"
    """type_ (str): Type of the background, always “fill”"""
    fill: "BackgroundFill"
    """fill ("BackgroundFill"): The background fill"""
    dark_theme_dimming: int
    """dark_theme_dimming (int): Dimming of the background in dark themes, as a percentage; 0-100"""


class BackgroundTypeWallpaper(BaseModel):
    """The background is a wallpaper in the JPEG format.

    https://core.telegram.org/bots/api/#backgroundtypewallpaper
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "wallpaper"
    """type_ (str): Type of the background, always “wallpaper”"""
    document: "Document"
    """document ("Document"): Document with the wallpaper"""
    dark_theme_dimming: int
    """dark_theme_dimming (int): Dimming of the background in dark themes, as a percentage; 0-100"""
    is_blurred: Optional[bool] = True
    """is_blurred (bool): *Optional*. *True*, if the wallpaper is downscaled to fit in a 450x450 square and then box-blurred with radius 12"""
    is_moving: Optional[bool] = True
    """is_moving (bool): *Optional*. *True*, if the background moves slightly when the device is tilted"""


class BackgroundTypePattern(BaseModel):
    """The background is a .PNG or .TGV (gzipped subset of SVG with MIME type “application/x-tgwallpattern”) pattern to be combined with the background fill chosen by the user.

    https://core.telegram.org/bots/api/#backgroundtypepattern
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "pattern"
    """type_ (str): Type of the background, always “pattern”"""
    document: "Document"
    """document ("Document"): Document with the pattern"""
    fill: "BackgroundFill"
    """fill ("BackgroundFill"): The background fill that is combined with the pattern"""
    intensity: int
    """intensity (int): Intensity of the pattern when it is shown above the filled background; 0-100"""
    is_inverted: Optional[bool] = True
    """is_inverted (bool): *Optional*. *True*, if the background fill must be applied only to the pattern itself. All other pixels are black in this case. For dark themes only"""
    is_moving: Optional[bool] = True
    """is_moving (bool): *Optional*. *True*, if the background moves slightly when the device is tilted"""


class BackgroundTypeChatTheme(BaseModel):
    """The background is taken directly from a built-in chat theme.

    https://core.telegram.org/bots/api/#backgroundtypechattheme
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "chat_theme"
    """type_ (str): Type of the background, always “chat_theme”"""
    theme_name: str
    """theme_name (str): Name of the chat theme, which is usually an emoji"""


class ChatBackground(BaseModel):
    """This object represents a chat background.

    https://core.telegram.org/bots/api/#chatbackground
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: "BackgroundType"
    """type_ ("BackgroundType"): Type of the background"""


class ForumTopicCreated(BaseModel):
    """This object represents a service message about a new forum topic created in the chat.

    https://core.telegram.org/bots/api/#forumtopiccreated
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    name: str
    """name (str): Name of the topic"""
    icon_color: int
    """icon_color (int): Color of the topic icon in RGB format"""
    icon_custom_emoji_id: Optional[str] = None
    """icon_custom_emoji_id (str): *Optional*. Unique identifier of the custom emoji shown as the topic icon"""


ForumTopicClosed = Any
"""This object represents a service message about a forum topic closed in the chat. Currently holds no information."""


class ForumTopicEdited(BaseModel):
    """This object represents a service message about an edited forum topic.

    https://core.telegram.org/bots/api/#forumtopicedited
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    name: Optional[str] = None
    """name (str): *Optional*. New name of the topic, if it was edited"""
    icon_custom_emoji_id: Optional[str] = None
    """icon_custom_emoji_id (str): *Optional*. New identifier of the custom emoji shown as the topic icon, if it was edited; an empty string if the icon was removed"""


ForumTopicReopened = Any
"""This object represents a service message about a forum topic reopened in the chat. Currently holds no information."""

GeneralForumTopicHidden = Any
"""This object represents a service message about General forum topic hidden in the chat. Currently holds no information."""

GeneralForumTopicUnhidden = Any
"""This object represents a service message about General forum topic unhidden in the chat. Currently holds no information."""


class SharedUser(BaseModel):
    """This object contains information about a user that was shared with the bot using a [KeyboardButtonRequestUsers](https://core.telegram.org/bots/api/#keyboardbuttonrequestusers) button.

    https://core.telegram.org/bots/api/#shareduser
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    user_id: int
    """user_id (int): Identifier of the shared user. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so 64-bit integers or double-precision float types are safe for storing these identifiers. The bot may not have access to the user and could be unable to use this identifier, unless the user is already known to the bot by some other means."""
    first_name: Optional[str] = None
    """first_name (str): *Optional*. First name of the user, if the name was requested by the bot"""
    last_name: Optional[str] = None
    """last_name (str): *Optional*. Last name of the user, if the name was requested by the bot"""
    username: Optional[str] = None
    """username (str): *Optional*. Username of the user, if the username was requested by the bot"""
    photo: Optional[List["PhotoSize"]] = None
    """photo (List["PhotoSize"]): *Optional*. Available sizes of the chat photo, if the photo was requested by the bot"""


class UsersShared(BaseModel):
    """This object contains information about the users whose identifiers were shared with the bot using a [KeyboardButtonRequestUsers](https://core.telegram.org/bots/api/#keyboardbuttonrequestusers) button.

    https://core.telegram.org/bots/api/#usersshared
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    request_id: int
    """request_id (int): Identifier of the request"""
    users: List["SharedUser"]
    """users (List["SharedUser"]): Information about users shared with the bot."""


class ChatShared(BaseModel):
    """This object contains information about a chat that was shared with the bot using a [KeyboardButtonRequestChat](https://core.telegram.org/bots/api/#keyboardbuttonrequestchat) button.

    https://core.telegram.org/bots/api/#chatshared
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    request_id: int
    """request_id (int): Identifier of the request"""
    chat_id: int
    """chat_id (int): Identifier of the shared chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot may not have access to the chat and could be unable to use this identifier, unless the chat is already known to the bot by some other means."""
    title: Optional[str] = None
    """title (str): *Optional*. Title of the chat, if the title was requested by the bot."""
    username: Optional[str] = None
    """username (str): *Optional*. Username of the chat, if the username was requested by the bot and available."""
    photo: Optional[List["PhotoSize"]] = None
    """photo (List["PhotoSize"]): *Optional*. Available sizes of the chat photo, if the photo was requested by the bot"""


class WriteAccessAllowed(BaseModel):
    """This object represents a service message about a user allowing a bot to write messages after adding it to the attachment menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method [requestWriteAccess](https://core.telegram.org/bots/webapps#initializing-mini-apps).

    https://core.telegram.org/bots/api/#writeaccessallowed
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    from_request: Optional[bool] = None
    """from_request (bool): *Optional*. True, if the access was granted after the user accepted an explicit request from a Web App sent by the method [requestWriteAccess](https://core.telegram.org/bots/webapps#initializing-mini-apps)"""
    web_app_name: Optional[str] = None
    """web_app_name (str): *Optional*. Name of the Web App, if the access was granted when the Web App was launched from a link"""
    from_attachment_menu: Optional[bool] = None
    """from_attachment_menu (bool): *Optional*. True, if the access was granted when the bot was added to the attachment or side menu"""


class VideoChatScheduled(BaseModel):
    """This object represents a service message about a video chat scheduled in the chat.

    https://core.telegram.org/bots/api/#videochatscheduled
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    start_date: int
    """start_date (int): Point in time (Unix timestamp) when the video chat is supposed to be started by a chat administrator"""


VideoChatStarted = Any
"""This object represents a service message about a video chat started in the chat. Currently holds no information."""


class VideoChatEnded(BaseModel):
    """This object represents a service message about a video chat ended in the chat.

    https://core.telegram.org/bots/api/#videochatended
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    duration: int
    """duration (int): Video chat duration in seconds"""


class VideoChatParticipantsInvited(BaseModel):
    """This object represents a service message about new members invited to a video chat.

    https://core.telegram.org/bots/api/#videochatparticipantsinvited
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    users: List["User"]
    """users (List["User"]): New members that were invited to the video chat"""


class GiveawayCreated(BaseModel):
    """This object represents a service message about the creation of a scheduled giveaway.

    https://core.telegram.org/bots/api/#giveawaycreated
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    prize_star_count: Optional[int] = None
    """prize_star_count (int): *Optional*. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only"""


class Giveaway(BaseModel):
    """This object represents a message about a scheduled giveaway.

    https://core.telegram.org/bots/api/#giveaway
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    chats: List["Chat"]
    """chats (List["Chat"]): The list of chats which the user must join to participate in the giveaway"""
    winners_selection_date: int
    """winners_selection_date (int): Point in time (Unix timestamp) when winners of the giveaway will be selected"""
    winner_count: int
    """winner_count (int): The number of users which are supposed to be selected as winners of the giveaway"""
    only_new_members: Optional[bool] = True
    """only_new_members (bool): *Optional*. *True*, if only users who join the chats after the giveaway started should be eligible to win"""
    has_public_winners: Optional[bool] = True
    """has_public_winners (bool): *Optional*. *True*, if the list of giveaway winners will be visible to everyone"""
    prize_description: Optional[str] = None
    """prize_description (str): *Optional*. Description of additional giveaway prize"""
    country_codes: Optional[List[str]] = None
    """country_codes (List[str]): *Optional*. A list of two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes indicating the countries from which eligible users for the giveaway must come. If empty, then all users can participate in the giveaway. Users with a phone number that was bought on Fragment can always participate in giveaways."""
    prize_star_count: Optional[int] = None
    """prize_star_count (int): *Optional*. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only"""
    premium_subscription_month_count: Optional[int] = None
    """premium_subscription_month_count (int): *Optional*. The number of months the Telegram Premium subscription won from the giveaway will be active for; for Telegram Premium giveaways only"""


class GiveawayWinners(BaseModel):
    """This object represents a message about the completion of a giveaway with public winners.

    https://core.telegram.org/bots/api/#giveawaywinners
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    chat: "Chat"
    """chat ("Chat"): The chat that created the giveaway"""
    giveaway_message_id: int
    """giveaway_message_id (int): Identifier of the message with the giveaway in the chat"""
    winners_selection_date: int
    """winners_selection_date (int): Point in time (Unix timestamp) when winners of the giveaway were selected"""
    winner_count: int
    """winner_count (int): Total number of winners in the giveaway"""
    winners: List["User"]
    """winners (List["User"]): List of up to 100 winners of the giveaway"""
    additional_chat_count: Optional[int] = None
    """additional_chat_count (int): *Optional*. The number of other chats the user had to join in order to be eligible for the giveaway"""
    prize_star_count: Optional[int] = None
    """prize_star_count (int): *Optional*. The number of Telegram Stars that were split between giveaway winners; for Telegram Star giveaways only"""
    premium_subscription_month_count: Optional[int] = None
    """premium_subscription_month_count (int): *Optional*. The number of months the Telegram Premium subscription won from the giveaway will be active for; for Telegram Premium giveaways only"""
    unclaimed_prize_count: Optional[int] = None
    """unclaimed_prize_count (int): *Optional*. Number of undistributed prizes"""
    only_new_members: Optional[bool] = True
    """only_new_members (bool): *Optional*. *True*, if only users who had joined the chats after the giveaway started were eligible to win"""
    was_refunded: Optional[bool] = True
    """was_refunded (bool): *Optional*. *True*, if the giveaway was canceled because the payment for it was refunded"""
    prize_description: Optional[str] = None
    """prize_description (str): *Optional*. Description of additional giveaway prize"""


class GiveawayCompleted(BaseModel):
    """This object represents a service message about the completion of a giveaway without public winners.

    https://core.telegram.org/bots/api/#giveawaycompleted
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    winner_count: int
    """winner_count (int): Number of winners in the giveaway"""
    unclaimed_prize_count: Optional[int] = None
    """unclaimed_prize_count (int): *Optional*. Number of undistributed prizes"""
    giveaway_message: Optional["Message"] = None
    """giveaway_message ("Message"): *Optional*. Message with the giveaway that was completed, if it wasn't deleted"""
    is_star_giveaway: Optional[bool] = True
    """is_star_giveaway (bool): *Optional*. *True*, if the giveaway is a Telegram Star giveaway. Otherwise, currently, the giveaway is a Telegram Premium giveaway."""


class LinkPreviewOptions(BaseModel):
    """Describes the options used for link preview generation.

    https://core.telegram.org/bots/api/#linkpreviewoptions
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    is_disabled: Optional[bool] = None
    """is_disabled (bool): *Optional*. *True*, if the link preview is disabled"""
    url: Optional[str] = None
    """url (str): *Optional*. URL to use for the link preview. If empty, then the first URL found in the message text will be used"""
    prefer_small_media: Optional[bool] = None
    """prefer_small_media (bool): *Optional*. *True*, if the media in the link preview is supposed to be shrunk; ignored if the URL isn't explicitly specified or media size change isn't supported for the preview"""
    prefer_large_media: Optional[bool] = None
    """prefer_large_media (bool): *Optional*. *True*, if the media in the link preview is supposed to be enlarged; ignored if the URL isn't explicitly specified or media size change isn't supported for the preview"""
    show_above_text: Optional[bool] = None
    """show_above_text (bool): *Optional*. *True*, if the link preview must be shown above the message text; otherwise, the link preview will be shown below the message text"""


class UserProfilePhotos(BaseModel):
    """This object represent a user's profile pictures.

    https://core.telegram.org/bots/api/#userprofilephotos
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    total_count: int
    """total_count (int): Total number of profile pictures the target user has"""
    photos: List[List["PhotoSize"]]
    """photos (List[List["PhotoSize"]]): Requested profile pictures (in up to 4 sizes each)"""


class File(BaseModel):
    """This object represents a file ready to be downloaded. The file can be downloaded via the link `https://api.telegram.org/file/bot<token>/<file_path>`. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling [getFile](https://core.telegram.org/bots/api/#getfile).

The maximum file size to download is 20 MB

    https://core.telegram.org/bots/api/#file
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    file_id: str
    """file_id (str): Identifier for this file, which can be used to download or reuse the file"""
    file_unique_id: str
    """file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file."""
    file_size: Optional[int] = None
    """file_size (int): *Optional*. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value."""
    file_path: Optional[str] = None
    """file_path (str): *Optional*. File path. Use `https://api.telegram.org/file/bot<token>/<file_path>` to get the file."""


class WebAppInfo(BaseModel):
    """Describes a [Web App](https://core.telegram.org/bots/webapps).

    https://core.telegram.org/bots/api/#webappinfo
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    url: str
    """url (str): An HTTPS URL of a Web App to be opened with additional data as specified in [Initializing Web Apps](https://core.telegram.org/bots/webapps#initializing-mini-apps)"""


class ReplyKeyboardMarkup(BaseModel):
    """This object represents a [custom keyboard](https://core.telegram.org/bots/features#keyboards) with reply options (see [Introduction to bots](https://core.telegram.org/bots/features#keyboards) for details and examples). Not supported in channels and for messages sent on behalf of a Telegram Business account.

    https://core.telegram.org/bots/api/#replykeyboardmarkup
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    keyboard: List[List["KeyboardButton"]]
    """keyboard (List[List["KeyboardButton"]]): Array of button rows, each represented by an Array of [KeyboardButton](https://core.telegram.org/bots/api/#keyboardbutton) objects"""
    is_persistent: Optional[bool] = None
    """is_persistent (bool): *Optional*. Requests clients to always show the keyboard when the regular keyboard is hidden. Defaults to *false*, in which case the custom keyboard can be hidden and opened with a keyboard icon."""
    resize_keyboard: Optional[bool] = None
    """resize_keyboard (bool): *Optional*. Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to *false*, in which case the custom keyboard is always of the same height as the app's standard keyboard."""
    one_time_keyboard: Optional[bool] = None
    """one_time_keyboard (bool): *Optional*. Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat - the user can press a special button in the input field to see the custom keyboard again. Defaults to *false*."""
    input_field_placeholder: Optional[str] = None
    """input_field_placeholder (str): *Optional*. The placeholder to be shown in the input field when the keyboard is active; 1-64 characters"""
    selective: Optional[bool] = None
    """selective (bool): *Optional*. Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the *text* of the [Message](https://core.telegram.org/bots/api/#message) object; 2) if the bot's message is a reply to a message in the same chat and forum topic, sender of the original message.  

*Example:* A user requests to change the bot's language, bot replies to the request with a keyboard to select the new language. Other users in the group don't see the keyboard."""


class KeyboardButton(BaseModel):
    """This object represents one button of the reply keyboard. At most one of the optional fields must be used to specify type of the button. For simple text buttons, *String* can be used instead of this object to specify the button text.

    https://core.telegram.org/bots/api/#keyboardbutton
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    text: str
    """text (str): Text of the button. If none of the optional fields are used, it will be sent as a message when the button is pressed"""
    request_users: Optional["KeyboardButtonRequestUsers"] = None
    """request_users ("KeyboardButtonRequestUsers"): *Optional.* If specified, pressing the button will open a list of suitable users. Identifiers of selected users will be sent to the bot in a “users_shared” service message. Available in private chats only."""
    request_chat: Optional["KeyboardButtonRequestChat"] = None
    """request_chat ("KeyboardButtonRequestChat"): *Optional.* If specified, pressing the button will open a list of suitable chats. Tapping on a chat will send its identifier to the bot in a “chat_shared” service message. Available in private chats only."""
    request_contact: Optional[bool] = None
    """request_contact (bool): *Optional*. If *True*, the user's phone number will be sent as a contact when the button is pressed. Available in private chats only."""
    request_location: Optional[bool] = None
    """request_location (bool): *Optional*. If *True*, the user's current location will be sent when the button is pressed. Available in private chats only."""
    request_poll: Optional["KeyboardButtonPollType"] = None
    """request_poll ("KeyboardButtonPollType"): *Optional*. If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Available in private chats only."""
    web_app: Optional["WebAppInfo"] = None
    """web_app ("WebAppInfo"): *Optional*. If specified, the described [Web App](https://core.telegram.org/bots/webapps) will be launched when the button is pressed. The Web App will be able to send a “web_app_data” service message. Available in private chats only."""


class KeyboardButtonRequestUsers(BaseModel):
    """This object defines the criteria used to request suitable users. Information about the selected users will be shared with the bot when the corresponding button is pressed. [More about requesting users »](https://core.telegram.org/bots/features#chat-and-user-selection)

    https://core.telegram.org/bots/api/#keyboardbuttonrequestusers
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    request_id: int
    """request_id (int): Signed 32-bit identifier of the request that will be received back in the [UsersShared](https://core.telegram.org/bots/api/#usersshared) object. Must be unique within the message"""
    user_is_bot: Optional[bool] = None
    """user_is_bot (bool): *Optional*. Pass *True* to request bots, pass *False* to request regular users. If not specified, no additional restrictions are applied."""
    user_is_premium: Optional[bool] = None
    """user_is_premium (bool): *Optional*. Pass *True* to request premium users, pass *False* to request non-premium users. If not specified, no additional restrictions are applied."""
    max_quantity: Optional[int] = 1
    """max_quantity (int): *Optional*. The maximum number of users to be selected; 1-10. Defaults to 1."""
    request_name: Optional[bool] = None
    """request_name (bool): *Optional*. Pass *True* to request the users' first and last names"""
    request_username: Optional[bool] = None
    """request_username (bool): *Optional*. Pass *True* to request the users' usernames"""
    request_photo: Optional[bool] = None
    """request_photo (bool): *Optional*. Pass *True* to request the users' photos"""


class KeyboardButtonRequestChat(BaseModel):
    """This object defines the criteria used to request a suitable chat. Information about the selected chat will be shared with the bot when the corresponding button is pressed. The bot will be granted requested rights in the chat if appropriate. [More about requesting chats »](https://core.telegram.org/bots/features#chat-and-user-selection).

    https://core.telegram.org/bots/api/#keyboardbuttonrequestchat
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    request_id: int
    """request_id (int): Signed 32-bit identifier of the request, which will be received back in the [ChatShared](https://core.telegram.org/bots/api/#chatshared) object. Must be unique within the message"""
    chat_is_channel: bool
    """chat_is_channel (bool): Pass *True* to request a channel chat, pass *False* to request a group or a supergroup chat."""
    chat_is_forum: Optional[bool] = None
    """chat_is_forum (bool): *Optional*. Pass *True* to request a forum supergroup, pass *False* to request a non-forum chat. If not specified, no additional restrictions are applied."""
    chat_has_username: Optional[bool] = None
    """chat_has_username (bool): *Optional*. Pass *True* to request a supergroup or a channel with a username, pass *False* to request a chat without a username. If not specified, no additional restrictions are applied."""
    chat_is_created: Optional[bool] = None
    """chat_is_created (bool): *Optional*. Pass *True* to request a chat owned by the user. Otherwise, no additional restrictions are applied."""
    user_administrator_rights: Optional["ChatAdministratorRights"] = None
    """user_administrator_rights ("ChatAdministratorRights"): *Optional*. A JSON-serialized object listing the required administrator rights of the user in the chat. The rights must be a superset of *bot_administrator_rights*. If not specified, no additional restrictions are applied."""
    bot_administrator_rights: Optional["ChatAdministratorRights"] = None
    """bot_administrator_rights ("ChatAdministratorRights"): *Optional*. A JSON-serialized object listing the required administrator rights of the bot in the chat. The rights must be a subset of *user_administrator_rights*. If not specified, no additional restrictions are applied."""
    bot_is_member: Optional[bool] = None
    """bot_is_member (bool): *Optional*. Pass *True* to request a chat with the bot as a member. Otherwise, no additional restrictions are applied."""
    request_title: Optional[bool] = None
    """request_title (bool): *Optional*. Pass *True* to request the chat's title"""
    request_username: Optional[bool] = None
    """request_username (bool): *Optional*. Pass *True* to request the chat's username"""
    request_photo: Optional[bool] = None
    """request_photo (bool): *Optional*. Pass *True* to request the chat's photo"""


class KeyboardButtonPollType(BaseModel):
    """This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed.

    https://core.telegram.org/bots/api/#keyboardbuttonpolltype
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: Optional[str] = None
    """type_ (str): *Optional*. If *quiz* is passed, the user will be allowed to create only polls in the quiz mode. If *regular* is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type."""


class ReplyKeyboardRemove(BaseModel):
    """Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see [ReplyKeyboardMarkup](https://core.telegram.org/bots/api/#replykeyboardmarkup)). Not supported in channels and for messages sent on behalf of a Telegram Business account.

    https://core.telegram.org/bots/api/#replykeyboardremove
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    remove_keyboard: bool = True
    """remove_keyboard (bool): Requests clients to remove the custom keyboard (user will not be able to summon this keyboard; if you want to hide the keyboard from sight but keep it accessible, use *one_time_keyboard* in [ReplyKeyboardMarkup](https://core.telegram.org/bots/api/#replykeyboardmarkup))"""
    selective: Optional[bool] = None
    """selective (bool): *Optional*. Use this parameter if you want to remove the keyboard for specific users only. Targets: 1) users that are @mentioned in the *text* of the [Message](https://core.telegram.org/bots/api/#message) object; 2) if the bot's message is a reply to a message in the same chat and forum topic, sender of the original message.  

*Example:* A user votes in a poll, bot returns confirmation message in reply to the vote and removes the keyboard for that user, while still showing the keyboard with poll options to users who haven't voted yet."""


class InlineKeyboardMarkup(BaseModel):
    """This object represents an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) that appears right next to the message it belongs to.

    https://core.telegram.org/bots/api/#inlinekeyboardmarkup
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    inline_keyboard: List[List["InlineKeyboardButton"]]
    """inline_keyboard (List[List["InlineKeyboardButton"]]): Array of button rows, each represented by an Array of [InlineKeyboardButton](https://core.telegram.org/bots/api/#inlinekeyboardbutton) objects"""


class InlineKeyboardButton(BaseModel):
    """This object represents one button of an inline keyboard. Exactly one of the optional fields must be used to specify type of the button.

    https://core.telegram.org/bots/api/#inlinekeyboardbutton
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    text: str
    """text (str): Label text on the button"""
    url: Optional[str] = None
    """url (str): *Optional*. HTTP or tg:// URL to be opened when the button is pressed. Links `tg://user?id=<user_id>` can be used to mention a user by their identifier without using a username, if this is allowed by their privacy settings."""
    callback_data: Optional[str] = None
    """callback_data (str): *Optional*. Data to be sent in a [callback query](https://core.telegram.org/bots/api/#callbackquery) to the bot when the button is pressed, 1-64 bytes"""
    web_app: Optional["WebAppInfo"] = None
    """web_app ("WebAppInfo"): *Optional*. Description of the [Web App](https://core.telegram.org/bots/webapps) that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method [answerWebAppQuery](https://core.telegram.org/bots/api/#answerwebappquery). Available only in private chats between a user and the bot. Not supported for messages sent on behalf of a Telegram Business account."""
    login_url: Optional["LoginUrl"] = None
    """login_url ("LoginUrl"): *Optional*. An HTTPS URL used to automatically authorize the user. Can be used as a replacement for the [Telegram Login Widget](https://core.telegram.org/widgets/login)."""
    switch_inline_query: Optional[str] = None
    """switch_inline_query (str): *Optional*. If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. May be empty, in which case just the bot's username will be inserted. Not supported for messages sent on behalf of a Telegram Business account."""
    switch_inline_query_current_chat: Optional[str] = None
    """switch_inline_query_current_chat (str): *Optional*. If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. May be empty, in which case only the bot's username will be inserted.  

This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting something from multiple options. Not supported in channels and for messages sent on behalf of a Telegram Business account."""
    switch_inline_query_chosen_chat: Optional["SwitchInlineQueryChosenChat"] = None
    """switch_inline_query_chosen_chat ("SwitchInlineQueryChosenChat"): *Optional*. If set, pressing the button will prompt the user to select one of their chats of the specified type, open that chat and insert the bot's username and the specified inline query in the input field. Not supported for messages sent on behalf of a Telegram Business account."""
    copy_text: Optional["CopyTextButton"] = None
    """copy_text ("CopyTextButton"): *Optional*. Description of the button that copies the specified text to the clipboard."""
    callback_game: Optional["CallbackGame"] = None
    """callback_game ("CallbackGame"): *Optional*. Description of the game that will be launched when the user presses the button.  

**NOTE:** This type of button **must** always be the first button in the first row."""
    pay: Optional[bool] = None
    """pay (bool): *Optional*. Specify *True*, to send a [Pay button](https://core.telegram.org/bots/api/#payments). Substrings “⭐” and “XTR” in the buttons's text will be replaced with a Telegram Star icon.  

**NOTE:** This type of button **must** always be the first button in the first row and can only be used in invoice messages."""


class LoginUrl(BaseModel):
    """This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the [Telegram Login Widget](https://core.telegram.org/widgets/login) when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in:

Telegram apps support these buttons as of [version 5.7](https://telegram.org/blog/privacy-discussions-web-bots#meet-seamless-web-bots).

Sample bot: [@discussbot](https://t.me/discussbot)

    https://core.telegram.org/bots/api/#loginurl
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    url: str
    """url (str): An HTTPS URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in [Receiving authorization data](https://core.telegram.org/widgets/login#receiving-authorization-data).  

**NOTE:** You **must** always check the hash of the received data to verify the authentication and the integrity of the data as described in [Checking authorization](https://core.telegram.org/widgets/login#checking-authorization)."""
    forward_text: Optional[str] = None
    """forward_text (str): *Optional*. New text of the button in forwarded messages."""
    bot_username: Optional[str] = None
    """bot_username (str): *Optional*. Username of a bot, which will be used for user authorization. See [Setting up a bot](https://core.telegram.org/widgets/login#setting-up-a-bot) for more details. If not specified, the current bot's username will be assumed. The *url*'s domain must be the same as the domain linked with the bot. See [Linking your domain to the bot](https://core.telegram.org/widgets/login#linking-your-domain-to-the-bot) for more details."""
    request_write_access: Optional[bool] = None
    """request_write_access (bool): *Optional*. Pass *True* to request the permission for your bot to send messages to the user."""


class SwitchInlineQueryChosenChat(BaseModel):
    """This object represents an inline button that switches the current user to inline mode in a chosen chat, with an optional default inline query.

    https://core.telegram.org/bots/api/#switchinlinequerychosenchat
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    query: Optional[str] = None
    """query (str): *Optional*. The default inline query to be inserted in the input field. If left empty, only the bot's username will be inserted"""
    allow_user_chats: Optional[bool] = None
    """allow_user_chats (bool): *Optional*. True, if private chats with users can be chosen"""
    allow_bot_chats: Optional[bool] = None
    """allow_bot_chats (bool): *Optional*. True, if private chats with bots can be chosen"""
    allow_group_chats: Optional[bool] = None
    """allow_group_chats (bool): *Optional*. True, if group and supergroup chats can be chosen"""
    allow_channel_chats: Optional[bool] = None
    """allow_channel_chats (bool): *Optional*. True, if channel chats can be chosen"""


class CopyTextButton(BaseModel):
    """This object represents an inline keyboard button that copies specified text to the clipboard.

    https://core.telegram.org/bots/api/#copytextbutton
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    text: str
    """text (str): The text to be copied to the clipboard; 1-256 characters"""


class CallbackQuery(BaseModel):
    """This object represents an incoming callback query from a callback button in an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards). If the button that originated the query was attached to a message sent by the bot, the field *message* will be present. If the button was attached to a message sent via the bot (in [inline mode](https://core.telegram.org/bots/api/#inline-mode)), the field *inline_message_id* will be present. Exactly one of the fields *data* or *game_short_name* will be present.

    https://core.telegram.org/bots/api/#callbackquery
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    id: str
    """id (str): Unique identifier for this query"""
    from_: "User"
    """from_ ("User"): Sender"""
    message: Optional["MaybeInaccessibleMessage"] = None
    """message ("MaybeInaccessibleMessage"): *Optional*. Message sent by the bot with the callback button that originated the query"""
    inline_message_id: Optional[str] = None
    """inline_message_id (str): *Optional*. Identifier of the message sent via the bot in inline mode, that originated the query."""
    chat_instance: str
    """chat_instance (str): Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in [games](https://core.telegram.org/bots/api/#games)."""
    data: Optional[str] = None
    """data (str): *Optional*. Data associated with the callback button. Be aware that the message originated the query can contain no callback buttons with this data."""
    game_short_name: Optional[str] = None
    """game_short_name (str): *Optional*. Short name of a [Game](https://core.telegram.org/bots/api/#games) to be returned, serves as the unique identifier for the game"""


class ForceReply(BaseModel):
    """Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice [privacy mode](https://core.telegram.org/bots/features#privacy-mode). Not supported in channels and for messages sent on behalf of a Telegram Business account.

    https://core.telegram.org/bots/api/#forcereply
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    force_reply: bool = True
    """force_reply (bool): Shows reply interface to the user, as if they manually selected the bot's message and tapped 'Reply'"""
    input_field_placeholder: Optional[str] = None
    """input_field_placeholder (str): *Optional*. The placeholder to be shown in the input field when the reply is active; 1-64 characters"""
    selective: Optional[bool] = None
    """selective (bool): *Optional*. Use this parameter if you want to force reply from specific users only. Targets: 1) users that are @mentioned in the *text* of the [Message](https://core.telegram.org/bots/api/#message) object; 2) if the bot's message is a reply to a message in the same chat and forum topic, sender of the original message."""


class ChatPhoto(BaseModel):
    """This object represents a chat photo.

    https://core.telegram.org/bots/api/#chatphoto
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    small_file_id: str
    """small_file_id (str): File identifier of small (160x160) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed."""
    small_file_unique_id: str
    """small_file_unique_id (str): Unique file identifier of small (160x160) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file."""
    big_file_id: str
    """big_file_id (str): File identifier of big (640x640) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed."""
    big_file_unique_id: str
    """big_file_unique_id (str): Unique file identifier of big (640x640) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file."""


class ChatInviteLink(BaseModel):
    """Represents an invite link for a chat.

    https://core.telegram.org/bots/api/#chatinvitelink
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    invite_link: str
    """invite_link (str): The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with “…”."""
    creator: "User"
    """creator ("User"): Creator of the link"""
    creates_join_request: bool
    """creates_join_request (bool): *True*, if users joining the chat via the link need to be approved by chat administrators"""
    is_primary: bool
    """is_primary (bool): *True*, if the link is primary"""
    is_revoked: bool
    """is_revoked (bool): *True*, if the link is revoked"""
    name: Optional[str] = None
    """name (str): *Optional*. Invite link name"""
    expire_date: Optional[int] = None
    """expire_date (int): *Optional*. Point in time (Unix timestamp) when the link will expire or has been expired"""
    member_limit: Optional[int] = None
    """member_limit (int): *Optional*. The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999"""
    pending_join_request_count: Optional[int] = None
    """pending_join_request_count (int): *Optional*. Number of pending join requests created using this link"""
    subscription_period: Optional[int] = None
    """subscription_period (int): *Optional*. The number of seconds the subscription will be active for before the next payment"""
    subscription_price: Optional[int] = None
    """subscription_price (int): *Optional*. The amount of Telegram Stars a user must pay initially and after each subsequent subscription period to be a member of the chat using the link"""


class ChatAdministratorRights(BaseModel):
    """Represents the rights of an administrator in a chat.

    https://core.telegram.org/bots/api/#chatadministratorrights
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    is_anonymous: bool
    """is_anonymous (bool): *True*, if the user's presence in the chat is hidden"""
    can_manage_chat: bool
    """can_manage_chat (bool): *True*, if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages and ignore slow mode. Implied by any other administrator privilege."""
    can_delete_messages: bool
    """can_delete_messages (bool): *True*, if the administrator can delete messages of other users"""
    can_manage_video_chats: bool
    """can_manage_video_chats (bool): *True*, if the administrator can manage video chats"""
    can_restrict_members: bool
    """can_restrict_members (bool): *True*, if the administrator can restrict, ban or unban chat members, or access supergroup statistics"""
    can_promote_members: bool
    """can_promote_members (bool): *True*, if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by the user)"""
    can_change_info: bool
    """can_change_info (bool): *True*, if the user is allowed to change the chat title, photo and other settings"""
    can_invite_users: bool
    """can_invite_users (bool): *True*, if the user is allowed to invite new users to the chat"""
    can_post_stories: bool
    """can_post_stories (bool): *True*, if the administrator can post stories to the chat"""
    can_edit_stories: bool
    """can_edit_stories (bool): *True*, if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat's story archive"""
    can_delete_stories: bool
    """can_delete_stories (bool): *True*, if the administrator can delete stories posted by other users"""
    can_post_messages: Optional[bool] = None
    """can_post_messages (bool): *Optional*. *True*, if the administrator can post messages in the channel, or access channel statistics; for channels only"""
    can_edit_messages: Optional[bool] = None
    """can_edit_messages (bool): *Optional*. *True*, if the administrator can edit messages of other users and can pin messages; for channels only"""
    can_pin_messages: Optional[bool] = None
    """can_pin_messages (bool): *Optional*. *True*, if the user is allowed to pin messages; for groups and supergroups only"""
    can_manage_topics: Optional[bool] = None
    """can_manage_topics (bool): *Optional*. *True*, if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only"""


class ChatMemberUpdated(BaseModel):
    """This object represents changes in the status of a chat member.

    https://core.telegram.org/bots/api/#chatmemberupdated
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    chat: "Chat"
    """chat ("Chat"): Chat the user belongs to"""
    from_: "User"
    """from_ ("User"): Performer of the action, which resulted in the change"""
    date: int
    """date (int): Date the change was done in Unix time"""
    old_chat_member: "ChatMember"
    """old_chat_member ("ChatMember"): Previous information about the chat member"""
    new_chat_member: "ChatMember"
    """new_chat_member ("ChatMember"): New information about the chat member"""
    invite_link: Optional["ChatInviteLink"] = None
    """invite_link ("ChatInviteLink"): *Optional*. Chat invite link, which was used by the user to join the chat; for joining by invite link events only."""
    via_join_request: Optional[bool] = None
    """via_join_request (bool): *Optional*. True, if the user joined the chat after sending a direct join request without using an invite link and being approved by an administrator"""
    via_chat_folder_invite_link: Optional[bool] = None
    """via_chat_folder_invite_link (bool): *Optional*. True, if the user joined the chat via a chat folder invite link"""


ChatMember = Union["ChatMemberOwner", "ChatMemberAdministrator",
                   "ChatMemberMember", "ChatMemberRestricted", "ChatMemberLeft", "ChatMemberBanned"]
"""This object contains information about one member of a chat. Currently, the following 6 types of chat members are supported:

* [ChatMemberOwner](https://core.telegram.org/bots/api/#chatmemberowner)
* [ChatMemberAdministrator](https://core.telegram.org/bots/api/#chatmemberadministrator)
* [ChatMemberMember](https://core.telegram.org/bots/api/#chatmembermember)
* [ChatMemberRestricted](https://core.telegram.org/bots/api/#chatmemberrestricted)
* [ChatMemberLeft](https://core.telegram.org/bots/api/#chatmemberleft)
* [ChatMemberBanned](https://core.telegram.org/bots/api/#chatmemberbanned)"""


class ChatMemberOwner(BaseModel):
    """Represents a [chat member](https://core.telegram.org/bots/api/#chatmember) that owns the chat and has all administrator privileges.

    https://core.telegram.org/bots/api/#chatmemberowner
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    status: str = "creator"
    """status (str): The member's status in the chat, always “creator”"""
    user: "User"
    """user ("User"): Information about the user"""
    is_anonymous: bool
    """is_anonymous (bool): *True*, if the user's presence in the chat is hidden"""
    custom_title: Optional[str] = None
    """custom_title (str): *Optional*. Custom title for this user"""


class ChatMemberAdministrator(BaseModel):
    """Represents a [chat member](https://core.telegram.org/bots/api/#chatmember) that has some additional privileges.

    https://core.telegram.org/bots/api/#chatmemberadministrator
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    status: str = "administrator"
    """status (str): The member's status in the chat, always “administrator”"""
    user: "User"
    """user ("User"): Information about the user"""
    can_be_edited: bool
    """can_be_edited (bool): *True*, if the bot is allowed to edit administrator privileges of that user"""
    is_anonymous: bool
    """is_anonymous (bool): *True*, if the user's presence in the chat is hidden"""
    can_manage_chat: bool
    """can_manage_chat (bool): *True*, if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages and ignore slow mode. Implied by any other administrator privilege."""
    can_delete_messages: bool
    """can_delete_messages (bool): *True*, if the administrator can delete messages of other users"""
    can_manage_video_chats: bool
    """can_manage_video_chats (bool): *True*, if the administrator can manage video chats"""
    can_restrict_members: bool
    """can_restrict_members (bool): *True*, if the administrator can restrict, ban or unban chat members, or access supergroup statistics"""
    can_promote_members: bool
    """can_promote_members (bool): *True*, if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by the user)"""
    can_change_info: bool
    """can_change_info (bool): *True*, if the user is allowed to change the chat title, photo and other settings"""
    can_invite_users: bool
    """can_invite_users (bool): *True*, if the user is allowed to invite new users to the chat"""
    can_post_stories: bool
    """can_post_stories (bool): *True*, if the administrator can post stories to the chat"""
    can_edit_stories: bool
    """can_edit_stories (bool): *True*, if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat's story archive"""
    can_delete_stories: bool
    """can_delete_stories (bool): *True*, if the administrator can delete stories posted by other users"""
    can_post_messages: Optional[bool] = None
    """can_post_messages (bool): *Optional*. *True*, if the administrator can post messages in the channel, or access channel statistics; for channels only"""
    can_edit_messages: Optional[bool] = None
    """can_edit_messages (bool): *Optional*. *True*, if the administrator can edit messages of other users and can pin messages; for channels only"""
    can_pin_messages: Optional[bool] = None
    """can_pin_messages (bool): *Optional*. *True*, if the user is allowed to pin messages; for groups and supergroups only"""
    can_manage_topics: Optional[bool] = None
    """can_manage_topics (bool): *Optional*. *True*, if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only"""
    custom_title: Optional[str] = None
    """custom_title (str): *Optional*. Custom title for this user"""


class ChatMemberMember(BaseModel):
    """Represents a [chat member](https://core.telegram.org/bots/api/#chatmember) that has no additional privileges or restrictions.

    https://core.telegram.org/bots/api/#chatmembermember
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    status: str = "member"
    """status (str): The member's status in the chat, always “member”"""
    user: "User"
    """user ("User"): Information about the user"""
    until_date: Optional[int] = None
    """until_date (int): *Optional*. Date when the user's subscription will expire; Unix time"""


class ChatMemberRestricted(BaseModel):
    """Represents a [chat member](https://core.telegram.org/bots/api/#chatmember) that is under certain restrictions in the chat. Supergroups only.

    https://core.telegram.org/bots/api/#chatmemberrestricted
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    status: str = "restricted"
    """status (str): The member's status in the chat, always “restricted”"""
    user: "User"
    """user ("User"): Information about the user"""
    is_member: bool
    """is_member (bool): *True*, if the user is a member of the chat at the moment of the request"""
    can_send_messages: bool
    """can_send_messages (bool): *True*, if the user is allowed to send text messages, contacts, giveaways, giveaway winners, invoices, locations and venues"""
    can_send_audios: bool
    """can_send_audios (bool): *True*, if the user is allowed to send audios"""
    can_send_documents: bool
    """can_send_documents (bool): *True*, if the user is allowed to send documents"""
    can_send_photos: bool
    """can_send_photos (bool): *True*, if the user is allowed to send photos"""
    can_send_videos: bool
    """can_send_videos (bool): *True*, if the user is allowed to send videos"""
    can_send_video_notes: bool
    """can_send_video_notes (bool): *True*, if the user is allowed to send video notes"""
    can_send_voice_notes: bool
    """can_send_voice_notes (bool): *True*, if the user is allowed to send voice notes"""
    can_send_polls: bool
    """can_send_polls (bool): *True*, if the user is allowed to send polls"""
    can_send_other_messages: bool
    """can_send_other_messages (bool): *True*, if the user is allowed to send animations, games, stickers and use inline bots"""
    can_add_web_page_previews: bool
    """can_add_web_page_previews (bool): *True*, if the user is allowed to add web page previews to their messages"""
    can_change_info: bool
    """can_change_info (bool): *True*, if the user is allowed to change the chat title, photo and other settings"""
    can_invite_users: bool
    """can_invite_users (bool): *True*, if the user is allowed to invite new users to the chat"""
    can_pin_messages: bool
    """can_pin_messages (bool): *True*, if the user is allowed to pin messages"""
    can_manage_topics: bool
    """can_manage_topics (bool): *True*, if the user is allowed to create forum topics"""
    until_date: int
    """until_date (int): Date when restrictions will be lifted for this user; Unix time. If 0, then the user is restricted forever"""


class ChatMemberLeft(BaseModel):
    """Represents a [chat member](https://core.telegram.org/bots/api/#chatmember) that isn't currently a member of the chat, but may join it themselves.

    https://core.telegram.org/bots/api/#chatmemberleft
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    status: str = "left"
    """status (str): The member's status in the chat, always “left”"""
    user: "User"
    """user ("User"): Information about the user"""


class ChatMemberBanned(BaseModel):
    """Represents a [chat member](https://core.telegram.org/bots/api/#chatmember) that was banned in the chat and can't return to the chat or view chat messages.

    https://core.telegram.org/bots/api/#chatmemberbanned
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    status: str = "kicked"
    """status (str): The member's status in the chat, always “kicked”"""
    user: "User"
    """user ("User"): Information about the user"""
    until_date: int
    """until_date (int): Date when restrictions will be lifted for this user; Unix time. If 0, then the user is banned forever"""


class ChatJoinRequest(BaseModel):
    """Represents a join request sent to a chat.

    https://core.telegram.org/bots/api/#chatjoinrequest
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    chat: "Chat"
    """chat ("Chat"): Chat to which the request was sent"""
    from_: "User"
    """from_ ("User"): User that sent the join request"""
    user_chat_id: int
    """user_chat_id (int): Identifier of a private chat with the user who sent the join request. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot can use this identifier for 5 minutes to send messages until the join request is processed, assuming no other administrator contacted the user."""
    date: int
    """date (int): Date the request was sent in Unix time"""
    bio: Optional[str] = None
    """bio (str): *Optional*. Bio of the user."""
    invite_link: Optional["ChatInviteLink"] = None
    """invite_link ("ChatInviteLink"): *Optional*. Chat invite link that was used by the user to send the join request"""


class ChatPermissions(BaseModel):
    """Describes actions that a non-administrator user is allowed to take in a chat.

    https://core.telegram.org/bots/api/#chatpermissions
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    can_send_messages: Optional[bool] = None
    """can_send_messages (bool): *Optional*. *True*, if the user is allowed to send text messages, contacts, giveaways, giveaway winners, invoices, locations and venues"""
    can_send_audios: Optional[bool] = None
    """can_send_audios (bool): *Optional*. *True*, if the user is allowed to send audios"""
    can_send_documents: Optional[bool] = None
    """can_send_documents (bool): *Optional*. *True*, if the user is allowed to send documents"""
    can_send_photos: Optional[bool] = None
    """can_send_photos (bool): *Optional*. *True*, if the user is allowed to send photos"""
    can_send_videos: Optional[bool] = None
    """can_send_videos (bool): *Optional*. *True*, if the user is allowed to send videos"""
    can_send_video_notes: Optional[bool] = None
    """can_send_video_notes (bool): *Optional*. *True*, if the user is allowed to send video notes"""
    can_send_voice_notes: Optional[bool] = None
    """can_send_voice_notes (bool): *Optional*. *True*, if the user is allowed to send voice notes"""
    can_send_polls: Optional[bool] = None
    """can_send_polls (bool): *Optional*. *True*, if the user is allowed to send polls"""
    can_send_other_messages: Optional[bool] = None
    """can_send_other_messages (bool): *Optional*. *True*, if the user is allowed to send animations, games, stickers and use inline bots"""
    can_add_web_page_previews: Optional[bool] = None
    """can_add_web_page_previews (bool): *Optional*. *True*, if the user is allowed to add web page previews to their messages"""
    can_change_info: Optional[bool] = None
    """can_change_info (bool): *Optional*. *True*, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups"""
    can_invite_users: Optional[bool] = None
    """can_invite_users (bool): *Optional*. *True*, if the user is allowed to invite new users to the chat"""
    can_pin_messages: Optional[bool] = None
    """can_pin_messages (bool): *Optional*. *True*, if the user is allowed to pin messages. Ignored in public supergroups"""
    can_manage_topics: Optional[bool] = None
    """can_manage_topics (bool): *Optional*. *True*, if the user is allowed to create forum topics. If omitted defaults to the value of can_pin_messages"""


class Birthdate(BaseModel):
    """Describes the birthdate of a user.

    https://core.telegram.org/bots/api/#birthdate
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    day: int
    """day (int): Day of the user's birth; 1-31"""
    month: int
    """month (int): Month of the user's birth; 1-12"""
    year: Optional[int] = None
    """year (int): *Optional*. Year of the user's birth"""


class BusinessIntro(BaseModel):
    """Contains information about the start page settings of a Telegram Business account.

    https://core.telegram.org/bots/api/#businessintro
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    title: Optional[str] = None
    """title (str): *Optional*. Title text of the business intro"""
    message: Optional[str] = None
    """message (str): *Optional*. Message text of the business intro"""
    sticker: Optional["Sticker"] = None
    """sticker ("Sticker"): *Optional*. Sticker of the business intro"""


class BusinessLocation(BaseModel):
    """Contains information about the location of a Telegram Business account.

    https://core.telegram.org/bots/api/#businesslocation
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    address: str
    """address (str): Address of the business"""
    location: Optional["Location"] = None
    """location ("Location"): *Optional*. Location of the business"""


class BusinessOpeningHoursInterval(BaseModel):
    """Describes an interval of time during which a business is open.

    https://core.telegram.org/bots/api/#businessopeninghoursinterval
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    opening_minute: int
    """opening_minute (int): The minute's sequence number in a week, starting on Monday, marking the start of the time interval during which the business is open; 0 - 7 * 24 * 60"""
    closing_minute: int
    """closing_minute (int): The minute's sequence number in a week, starting on Monday, marking the end of the time interval during which the business is open; 0 - 8 * 24 * 60"""


class BusinessOpeningHours(BaseModel):
    """Describes the opening hours of a business.

    https://core.telegram.org/bots/api/#businessopeninghours
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    time_zone_name: str
    """time_zone_name (str): Unique name of the time zone for which the opening hours are defined"""
    opening_hours: List["BusinessOpeningHoursInterval"]
    """opening_hours (List["BusinessOpeningHoursInterval"]): List of time intervals describing business opening hours"""


class ChatLocation(BaseModel):
    """Represents a location to which a chat is connected.

    https://core.telegram.org/bots/api/#chatlocation
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    location: "Location"
    """location ("Location"): The location to which the supergroup is connected. Can't be a live location."""
    address: str
    """address (str): Location address; 1-64 characters, as defined by the chat owner"""


ReactionType = Union["ReactionTypeEmoji",
                     "ReactionTypeCustomEmoji", "ReactionTypePaid"]
"""This object describes the type of a reaction. Currently, it can be one of

* [ReactionTypeEmoji](https://core.telegram.org/bots/api/#reactiontypeemoji)
* [ReactionTypeCustomEmoji](https://core.telegram.org/bots/api/#reactiontypecustomemoji)
* [ReactionTypePaid](https://core.telegram.org/bots/api/#reactiontypepaid)"""


class ReactionTypeEmoji(BaseModel):
    """The reaction is based on an emoji.

    https://core.telegram.org/bots/api/#reactiontypeemoji
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "emoji"
    """type_ (str): Type of the reaction, always “emoji”"""
    emoji: str
    """emoji (str): Reaction emoji. Currently, it can be one of '👍', '👎', '❤', '🔥', '🥰', '👏', '😁', '🤔', '🤯', '😱', '🤬', '😢', '🎉', '🤩', '🤮', '💩', '🙏', '👌', '🕊', '🤡', '🥱', '🥴', '😍', '🐳', '❤‍🔥', '🌚', '🌭', '💯', '🤣', '⚡', '🍌', '🏆', '💔', '🤨', '😐', '🍓', '🍾', '💋', '🖕', '😈', '😴', '😭', '🤓', '👻', '👨‍💻', '👀', '🎃', '🙈', '😇', '😨', '🤝', '✍', '🤗', '🫡', '🎅', '🎄', '☃', '💅', '🤪', '🗿', '🆒', '💘', '🙉', '🦄', '😘', '💊', '🙊', '😎', '👾', '🤷‍♂', '🤷', '🤷‍♀', '😡'"""


class ReactionTypeCustomEmoji(BaseModel):
    """The reaction is based on a custom emoji.

    https://core.telegram.org/bots/api/#reactiontypecustomemoji
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "custom_emoji"
    """type_ (str): Type of the reaction, always “custom_emoji”"""
    custom_emoji_id: str
    """custom_emoji_id (str): Custom emoji identifier"""


class ReactionTypePaid(BaseModel):
    """The reaction is paid.

    https://core.telegram.org/bots/api/#reactiontypepaid
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "paid"
    """type_ (str): Type of the reaction, always “paid”"""


class ReactionCount(BaseModel):
    """Represents a reaction added to a message along with the number of times it was added.

    https://core.telegram.org/bots/api/#reactioncount
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: "ReactionType"
    """type_ ("ReactionType"): Type of the reaction"""
    total_count: int
    """total_count (int): Number of times the reaction was added"""


class MessageReactionUpdated(BaseModel):
    """This object represents a change of a reaction on a message performed by a user.

    https://core.telegram.org/bots/api/#messagereactionupdated
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    chat: "Chat"
    """chat ("Chat"): The chat containing the message the user reacted to"""
    message_id: int
    """message_id (int): Unique identifier of the message inside the chat"""
    user: Optional["User"] = None
    """user ("User"): *Optional*. The user that changed the reaction, if the user isn't anonymous"""
    actor_chat: Optional["Chat"] = None
    """actor_chat ("Chat"): *Optional*. The chat on behalf of which the reaction was changed, if the user is anonymous"""
    date: int
    """date (int): Date of the change in Unix time"""
    old_reaction: List["ReactionType"]
    """old_reaction (List["ReactionType"]): Previous list of reaction types that were set by the user"""
    new_reaction: List["ReactionType"]
    """new_reaction (List["ReactionType"]): New list of reaction types that have been set by the user"""


class MessageReactionCountUpdated(BaseModel):
    """This object represents reaction changes on a message with anonymous reactions.

    https://core.telegram.org/bots/api/#messagereactioncountupdated
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    chat: "Chat"
    """chat ("Chat"): The chat containing the message"""
    message_id: int
    """message_id (int): Unique message identifier inside the chat"""
    date: int
    """date (int): Date of the change in Unix time"""
    reactions: List["ReactionCount"]
    """reactions (List["ReactionCount"]): List of reactions that are present on the message"""


class ForumTopic(BaseModel):
    """This object represents a forum topic.

    https://core.telegram.org/bots/api/#forumtopic
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    message_thread_id: int
    """message_thread_id (int): Unique identifier of the forum topic"""
    name: str
    """name (str): Name of the topic"""
    icon_color: int
    """icon_color (int): Color of the topic icon in RGB format"""
    icon_custom_emoji_id: Optional[str] = None
    """icon_custom_emoji_id (str): *Optional*. Unique identifier of the custom emoji shown as the topic icon"""


class BotCommand(BaseModel):
    """This object represents a bot command.

    https://core.telegram.org/bots/api/#botcommand
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    command: str
    """command (str): Text of the command; 1-32 characters. Can contain only lowercase English letters, digits and underscores."""
    description: str
    """description (str): Description of the command; 1-256 characters."""


BotCommandScope = Union["BotCommandScopeDefault", "BotCommandScopeAllPrivateChats", "BotCommandScopeAllGroupChats",
                        "BotCommandScopeAllChatAdministrators", "BotCommandScopeChat", "BotCommandScopeChatAdministrators", "BotCommandScopeChatMember"]
"""This object represents the scope to which bot commands are applied. Currently, the following 7 scopes are supported:

* [BotCommandScopeDefault](https://core.telegram.org/bots/api/#botcommandscopedefault)
* [BotCommandScopeAllPrivateChats](https://core.telegram.org/bots/api/#botcommandscopeallprivatechats)
* [BotCommandScopeAllGroupChats](https://core.telegram.org/bots/api/#botcommandscopeallgroupchats)
* [BotCommandScopeAllChatAdministrators](https://core.telegram.org/bots/api/#botcommandscopeallchatadministrators)
* [BotCommandScopeChat](https://core.telegram.org/bots/api/#botcommandscopechat)
* [BotCommandScopeChatAdministrators](https://core.telegram.org/bots/api/#botcommandscopechatadministrators)
* [BotCommandScopeChatMember](https://core.telegram.org/bots/api/#botcommandscopechatmember)"""


class BotCommandScopeDefault(BaseModel):
    """Represents the default [scope](https://core.telegram.org/bots/api/#botcommandscope) of bot commands. Default commands are used if no commands with a [narrower scope](https://core.telegram.org/bots/api/#determining-list-of-commands) are specified for the user.

    https://core.telegram.org/bots/api/#botcommandscopedefault
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "default"
    """type_ (str): Scope type, must be *default*"""


class BotCommandScopeAllPrivateChats(BaseModel):
    """Represents the [scope](https://core.telegram.org/bots/api/#botcommandscope) of bot commands, covering all private chats.

    https://core.telegram.org/bots/api/#botcommandscopeallprivatechats
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "all_private_chats"
    """type_ (str): Scope type, must be *all_private_chats*"""


class BotCommandScopeAllGroupChats(BaseModel):
    """Represents the [scope](https://core.telegram.org/bots/api/#botcommandscope) of bot commands, covering all group and supergroup chats.

    https://core.telegram.org/bots/api/#botcommandscopeallgroupchats
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "all_group_chats"
    """type_ (str): Scope type, must be *all_group_chats*"""


class BotCommandScopeAllChatAdministrators(BaseModel):
    """Represents the [scope](https://core.telegram.org/bots/api/#botcommandscope) of bot commands, covering all group and supergroup chat administrators.

    https://core.telegram.org/bots/api/#botcommandscopeallchatadministrators
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "all_chat_administrators"
    """type_ (str): Scope type, must be *all_chat_administrators*"""


class BotCommandScopeChat(BaseModel):
    """Represents the [scope](https://core.telegram.org/bots/api/#botcommandscope) of bot commands, covering a specific chat.

    https://core.telegram.org/bots/api/#botcommandscopechat
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "chat"
    """type_ (str): Scope type, must be *chat*"""
    chat_id: Union[int, str]
    """chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)"""


class BotCommandScopeChatAdministrators(BaseModel):
    """Represents the [scope](https://core.telegram.org/bots/api/#botcommandscope) of bot commands, covering all administrators of a specific group or supergroup chat.

    https://core.telegram.org/bots/api/#botcommandscopechatadministrators
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "chat_administrators"
    """type_ (str): Scope type, must be *chat_administrators*"""
    chat_id: Union[int, str]
    """chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)"""


class BotCommandScopeChatMember(BaseModel):
    """Represents the [scope](https://core.telegram.org/bots/api/#botcommandscope) of bot commands, covering a specific member of a group or supergroup chat.

    https://core.telegram.org/bots/api/#botcommandscopechatmember
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "chat_member"
    """type_ (str): Scope type, must be *chat_member*"""
    chat_id: Union[int, str]
    """chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)"""
    user_id: int
    """user_id (int): Unique identifier of the target user"""


class BotName(BaseModel):
    """This object represents the bot's name.

    https://core.telegram.org/bots/api/#botname
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    name: str
    """name (str): The bot's name"""


class BotDescription(BaseModel):
    """This object represents the bot's description.

    https://core.telegram.org/bots/api/#botdescription
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    description: str
    """description (str): The bot's description"""


class BotShortDescription(BaseModel):
    """This object represents the bot's short description.

    https://core.telegram.org/bots/api/#botshortdescription
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    short_description: str
    """short_description (str): The bot's short description"""


MenuButton = Union["MenuButtonCommands",
                   "MenuButtonWebApp", "MenuButtonDefault"]
"""This object describes the bot's menu button in a private chat. It should be one of

* [MenuButtonCommands](https://core.telegram.org/bots/api/#menubuttoncommands)
* [MenuButtonWebApp](https://core.telegram.org/bots/api/#menubuttonwebapp)
* [MenuButtonDefault](https://core.telegram.org/bots/api/#menubuttondefault)"""


class MenuButtonCommands(BaseModel):
    """Represents a menu button, which opens the bot's list of commands.

    https://core.telegram.org/bots/api/#menubuttoncommands
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "commands"
    """type_ (str): Type of the button, must be *commands*"""


class MenuButtonWebApp(BaseModel):
    """Represents a menu button, which launches a [Web App](https://core.telegram.org/bots/webapps).

    https://core.telegram.org/bots/api/#menubuttonwebapp
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "web_app"
    """type_ (str): Type of the button, must be *web_app*"""
    text: str
    """text (str): Text on the button"""
    web_app: "WebAppInfo"
    """web_app ("WebAppInfo"): Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method [answerWebAppQuery](https://core.telegram.org/bots/api/#answerwebappquery). Alternatively, a `t.me` link to a Web App of the bot can be specified in the object instead of the Web App's URL, in which case the Web App will be opened as if the user pressed the link."""


class MenuButtonDefault(BaseModel):
    """Describes that no specific value for the menu button was set.

    https://core.telegram.org/bots/api/#menubuttondefault
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "default"
    """type_ (str): Type of the button, must be *default*"""


ChatBoostSource = Union["ChatBoostSourcePremium",
                        "ChatBoostSourceGiftCode", "ChatBoostSourceGiveaway"]
"""This object describes the source of a chat boost. It can be one of

* [ChatBoostSourcePremium](https://core.telegram.org/bots/api/#chatboostsourcepremium)
* [ChatBoostSourceGiftCode](https://core.telegram.org/bots/api/#chatboostsourcegiftcode)
* [ChatBoostSourceGiveaway](https://core.telegram.org/bots/api/#chatboostsourcegiveaway)"""


class ChatBoostSourcePremium(BaseModel):
    """The boost was obtained by subscribing to Telegram Premium or by gifting a Telegram Premium subscription to another user.

    https://core.telegram.org/bots/api/#chatboostsourcepremium
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    source: str = "premium"
    """source (str): Source of the boost, always “premium”"""
    user: "User"
    """user ("User"): User that boosted the chat"""


class ChatBoostSourceGiftCode(BaseModel):
    """The boost was obtained by the creation of Telegram Premium gift codes to boost a chat. Each such code boosts the chat 4 times for the duration of the corresponding Telegram Premium subscription.

    https://core.telegram.org/bots/api/#chatboostsourcegiftcode
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    source: str = "gift_code"
    """source (str): Source of the boost, always “gift_code”"""
    user: "User"
    """user ("User"): User for which the gift code was created"""


class ChatBoostSourceGiveaway(BaseModel):
    """The boost was obtained by the creation of a Telegram Premium or a Telegram Star giveaway. This boosts the chat 4 times for the duration of the corresponding Telegram Premium subscription for Telegram Premium giveaways and *prize_star_count* / 500 times for one year for Telegram Star giveaways.

    https://core.telegram.org/bots/api/#chatboostsourcegiveaway
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    source: str = "giveaway"
    """source (str): Source of the boost, always “giveaway”"""
    giveaway_message_id: int
    """giveaway_message_id (int): Identifier of a message in the chat with the giveaway; the message could have been deleted already. May be 0 if the message isn't sent yet."""
    user: Optional["User"] = None
    """user ("User"): *Optional*. User that won the prize in the giveaway if any; for Telegram Premium giveaways only"""
    prize_star_count: Optional[int] = None
    """prize_star_count (int): *Optional*. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only"""
    is_unclaimed: Optional[bool] = True
    """is_unclaimed (bool): *Optional*. True, if the giveaway was completed, but there was no user to win the prize"""


class ChatBoost(BaseModel):
    """This object contains information about a chat boost.

    https://core.telegram.org/bots/api/#chatboost
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    boost_id: str
    """boost_id (str): Unique identifier of the boost"""
    add_date: int
    """add_date (int): Point in time (Unix timestamp) when the chat was boosted"""
    expiration_date: int
    """expiration_date (int): Point in time (Unix timestamp) when the boost will automatically expire, unless the booster's Telegram Premium subscription is prolonged"""
    source: "ChatBoostSource"
    """source ("ChatBoostSource"): Source of the added boost"""


class ChatBoostUpdated(BaseModel):
    """This object represents a boost added to a chat or changed.

    https://core.telegram.org/bots/api/#chatboostupdated
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    chat: "Chat"
    """chat ("Chat"): Chat which was boosted"""
    boost: "ChatBoost"
    """boost ("ChatBoost"): Information about the chat boost"""


class ChatBoostRemoved(BaseModel):
    """This object represents a boost removed from a chat.

    https://core.telegram.org/bots/api/#chatboostremoved
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    chat: "Chat"
    """chat ("Chat"): Chat which was boosted"""
    boost_id: str
    """boost_id (str): Unique identifier of the boost"""
    remove_date: int
    """remove_date (int): Point in time (Unix timestamp) when the boost was removed"""
    source: "ChatBoostSource"
    """source ("ChatBoostSource"): Source of the removed boost"""


class UserChatBoosts(BaseModel):
    """This object represents a list of boosts added to a chat by a user.

    https://core.telegram.org/bots/api/#userchatboosts
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    boosts: List["ChatBoost"]
    """boosts (List["ChatBoost"]): The list of boosts added to the chat by the user"""


class BusinessConnection(BaseModel):
    """Describes the connection of the bot with a business account.

    https://core.telegram.org/bots/api/#businessconnection
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    id: str
    """id (str): Unique identifier of the business connection"""
    user: "User"
    """user ("User"): Business account user that created the business connection"""
    user_chat_id: int
    """user_chat_id (int): Identifier of a private chat with the user who created the business connection. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier."""
    date: int
    """date (int): Date the connection was established in Unix time"""
    can_reply: bool
    """can_reply (bool): True, if the bot can act on behalf of the business account in chats that were active in the last 24 hours"""
    is_enabled: bool
    """is_enabled (bool): True, if the connection is active"""


class BusinessMessagesDeleted(BaseModel):
    """This object is received when messages are deleted from a connected business account.

    https://core.telegram.org/bots/api/#businessmessagesdeleted
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    business_connection_id: str
    """business_connection_id (str): Unique identifier of the business connection"""
    chat: "Chat"
    """chat ("Chat"): Information about a chat in the business account. The bot may not have access to the chat or the corresponding user."""
    message_ids: List[int]
    """message_ids (List[int]): The list of identifiers of deleted messages in the chat of the business account"""


class ResponseParameters(BaseModel):
    """Describes why a request was unsuccessful.

    https://core.telegram.org/bots/api/#responseparameters
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    migrate_to_chat_id: Optional[int] = None
    """migrate_to_chat_id (int): *Optional*. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier."""
    retry_after: Optional[int] = None
    """retry_after (int): *Optional*. In case of exceeding flood control, the number of seconds left to wait before the request can be repeated"""


InputMedia = Union["InputMediaAnimation", "InputMediaDocument",
                   "InputMediaAudio", "InputMediaPhoto", "InputMediaVideo"]
"""This object represents the content of a media message to be sent. It should be one of

* [InputMediaAnimation](https://core.telegram.org/bots/api/#inputmediaanimation)
* [InputMediaDocument](https://core.telegram.org/bots/api/#inputmediadocument)
* [InputMediaAudio](https://core.telegram.org/bots/api/#inputmediaaudio)
* [InputMediaPhoto](https://core.telegram.org/bots/api/#inputmediaphoto)
* [InputMediaVideo](https://core.telegram.org/bots/api/#inputmediavideo)"""


class InputMediaPhoto(BaseModel):
    """Represents a photo to be sent.

    https://core.telegram.org/bots/api/#inputmediaphoto
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "photo"
    """type_ (str): Type of the result, must be *photo*"""
    media: str
    """media (str): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)"""
    caption: Optional[str] = None
    """caption (str): *Optional*. Caption of the photo to be sent, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = None
    """parse_mode (str): *Optional*. Mode for parsing entities in the photo caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details."""
    caption_entities: Optional[List["MessageEntity"]] = None
    """caption_entities (List["MessageEntity"]): *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*"""
    show_caption_above_media: Optional[bool] = None
    """show_caption_above_media (bool): *Optional*. Pass *True*, if the caption must be shown above the message media"""
    has_spoiler: Optional[bool] = None
    """has_spoiler (bool): *Optional*. Pass *True* if the photo needs to be covered with a spoiler animation"""


class InputMediaVideo(BaseModel):
    """Represents a video to be sent.

    https://core.telegram.org/bots/api/#inputmediavideo
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "video"
    """type_ (str): Type of the result, must be *video*"""
    media: str
    """media (str): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)"""
    thumbnail: Optional[str] = None
    """thumbnail (str): *Optional*. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)"""
    cover: Optional[str] = None
    """cover (str): *Optional*. Cover for the video in the message. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)"""
    start_timestamp: Optional[int] = None
    """start_timestamp (int): *Optional*. Start timestamp for the video in the message"""
    caption: Optional[str] = None
    """caption (str): *Optional*. Caption of the video to be sent, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = None
    """parse_mode (str): *Optional*. Mode for parsing entities in the video caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details."""
    caption_entities: Optional[List["MessageEntity"]] = None
    """caption_entities (List["MessageEntity"]): *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*"""
    show_caption_above_media: Optional[bool] = None
    """show_caption_above_media (bool): *Optional*. Pass *True*, if the caption must be shown above the message media"""
    width: Optional[int] = None
    """width (int): *Optional*. Video width"""
    height: Optional[int] = None
    """height (int): *Optional*. Video height"""
    duration: Optional[int] = None
    """duration (int): *Optional*. Video duration in seconds"""
    supports_streaming: Optional[bool] = None
    """supports_streaming (bool): *Optional*. Pass *True* if the uploaded video is suitable for streaming"""
    has_spoiler: Optional[bool] = None
    """has_spoiler (bool): *Optional*. Pass *True* if the video needs to be covered with a spoiler animation"""


class InputMediaAnimation(BaseModel):
    """Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.

    https://core.telegram.org/bots/api/#inputmediaanimation
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "animation"
    """type_ (str): Type of the result, must be *animation*"""
    media: str
    """media (str): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)"""
    thumbnail: Optional[str] = None
    """thumbnail (str): *Optional*. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)"""
    caption: Optional[str] = None
    """caption (str): *Optional*. Caption of the animation to be sent, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = None
    """parse_mode (str): *Optional*. Mode for parsing entities in the animation caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details."""
    caption_entities: Optional[List["MessageEntity"]] = None
    """caption_entities (List["MessageEntity"]): *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*"""
    show_caption_above_media: Optional[bool] = None
    """show_caption_above_media (bool): *Optional*. Pass *True*, if the caption must be shown above the message media"""
    width: Optional[int] = None
    """width (int): *Optional*. Animation width"""
    height: Optional[int] = None
    """height (int): *Optional*. Animation height"""
    duration: Optional[int] = None
    """duration (int): *Optional*. Animation duration in seconds"""
    has_spoiler: Optional[bool] = None
    """has_spoiler (bool): *Optional*. Pass *True* if the animation needs to be covered with a spoiler animation"""


class InputMediaAudio(BaseModel):
    """Represents an audio file to be treated as music to be sent.

    https://core.telegram.org/bots/api/#inputmediaaudio
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "audio"
    """type_ (str): Type of the result, must be *audio*"""
    media: str
    """media (str): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)"""
    thumbnail: Optional[str] = None
    """thumbnail (str): *Optional*. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)"""
    caption: Optional[str] = None
    """caption (str): *Optional*. Caption of the audio to be sent, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = None
    """parse_mode (str): *Optional*. Mode for parsing entities in the audio caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details."""
    caption_entities: Optional[List["MessageEntity"]] = None
    """caption_entities (List["MessageEntity"]): *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*"""
    duration: Optional[int] = None
    """duration (int): *Optional*. Duration of the audio in seconds"""
    performer: Optional[str] = None
    """performer (str): *Optional*. Performer of the audio"""
    title: Optional[str] = None
    """title (str): *Optional*. Title of the audio"""


class InputMediaDocument(BaseModel):
    """Represents a general file to be sent.

    https://core.telegram.org/bots/api/#inputmediadocument
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "document"
    """type_ (str): Type of the result, must be *document*"""
    media: str
    """media (str): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)"""
    thumbnail: Optional[str] = None
    """thumbnail (str): *Optional*. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)"""
    caption: Optional[str] = None
    """caption (str): *Optional*. Caption of the document to be sent, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = None
    """parse_mode (str): *Optional*. Mode for parsing entities in the document caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details."""
    caption_entities: Optional[List["MessageEntity"]] = None
    """caption_entities (List["MessageEntity"]): *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*"""
    disable_content_type_detection: Optional[bool] = None
    """disable_content_type_detection (bool): *Optional*. Disables automatic server-side content type detection for files uploaded using multipart/form-data. Always *True*, if the document is sent as part of an album."""


InputFile = Any
"""This object represents the contents of a file to be uploaded. Must be posted using multipart/form-data in the usual way that files are uploaded via the browser."""

InputPaidMedia = Union["InputPaidMediaPhoto", "InputPaidMediaVideo"]
"""This object describes the paid media to be sent. Currently, it can be one of

* [InputPaidMediaPhoto](https://core.telegram.org/bots/api/#inputpaidmediaphoto)
* [InputPaidMediaVideo](https://core.telegram.org/bots/api/#inputpaidmediavideo)"""


class InputPaidMediaPhoto(BaseModel):
    """The paid media to send is a photo.

    https://core.telegram.org/bots/api/#inputpaidmediaphoto
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "photo"
    """type_ (str): Type of the media, must be *photo*"""
    media: str
    """media (str): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)"""


class InputPaidMediaVideo(BaseModel):
    """The paid media to send is a video.

    https://core.telegram.org/bots/api/#inputpaidmediavideo
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "video"
    """type_ (str): Type of the media, must be *video*"""
    media: str
    """media (str): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)"""
    thumbnail: Optional[str] = None
    """thumbnail (str): *Optional*. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)"""
    cover: Optional[str] = None
    """cover (str): *Optional*. Cover for the video in the message. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)"""
    start_timestamp: Optional[int] = None
    """start_timestamp (int): *Optional*. Start timestamp for the video in the message"""
    width: Optional[int] = None
    """width (int): *Optional*. Video width"""
    height: Optional[int] = None
    """height (int): *Optional*. Video height"""
    duration: Optional[int] = None
    """duration (int): *Optional*. Video duration in seconds"""
    supports_streaming: Optional[bool] = None
    """supports_streaming (bool): *Optional*. Pass *True* if the uploaded video is suitable for streaming"""


class Sticker(BaseModel):
    """This object represents a sticker.

    https://core.telegram.org/bots/api/#sticker
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    file_id: str
    """file_id (str): Identifier for this file, which can be used to download or reuse the file"""
    file_unique_id: str
    """file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file."""
    type_: str
    """type_ (str): Type of the sticker, currently one of “regular”, “mask”, “custom_emoji”. The type of the sticker is independent from its format, which is determined by the fields *is_animated* and *is_video*."""
    width: int
    """width (int): Sticker width"""
    height: int
    """height (int): Sticker height"""
    is_animated: bool
    """is_animated (bool): *True*, if the sticker is [animated](https://telegram.org/blog/animated-stickers)"""
    is_video: bool
    """is_video (bool): *True*, if the sticker is a [video sticker](https://telegram.org/blog/video-stickers-better-reactions)"""
    thumbnail: Optional["PhotoSize"] = None
    """thumbnail ("PhotoSize"): *Optional*. Sticker thumbnail in the .WEBP or .JPG format"""
    emoji: Optional[str] = None
    """emoji (str): *Optional*. Emoji associated with the sticker"""
    set_name: Optional[str] = None
    """set_name (str): *Optional*. Name of the sticker set to which the sticker belongs"""
    premium_animation: Optional["File"] = None
    """premium_animation ("File"): *Optional*. For premium regular stickers, premium animation for the sticker"""
    mask_position: Optional["MaskPosition"] = None
    """mask_position ("MaskPosition"): *Optional*. For mask stickers, the position where the mask should be placed"""
    custom_emoji_id: Optional[str] = None
    """custom_emoji_id (str): *Optional*. For custom emoji stickers, unique identifier of the custom emoji"""
    needs_repainting: Optional[bool] = True
    """needs_repainting (bool): *Optional*. *True*, if the sticker must be repainted to a text color in messages, the color of the Telegram Premium badge in emoji status, white color on chat photos, or another appropriate color in other places"""
    file_size: Optional[int] = None
    """file_size (int): *Optional*. File size in bytes"""


class StickerSet(BaseModel):
    """This object represents a sticker set.

    https://core.telegram.org/bots/api/#stickerset
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    name: str
    """name (str): Sticker set name"""
    title: str
    """title (str): Sticker set title"""
    sticker_type: str
    """sticker_type (str): Type of stickers in the set, currently one of “regular”, “mask”, “custom_emoji”"""
    stickers: List["Sticker"]
    """stickers (List["Sticker"]): List of all set stickers"""
    thumbnail: Optional["PhotoSize"] = None
    """thumbnail ("PhotoSize"): *Optional*. Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format"""


class MaskPosition(BaseModel):
    """This object describes the position on faces where a mask should be placed by default.

    https://core.telegram.org/bots/api/#maskposition
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    point: str
    """point (str): The part of the face relative to which the mask should be placed. One of “forehead”, “eyes”, “mouth”, or “chin”."""
    x_shift: float
    """x_shift (float): Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example, choosing -1.0 will place mask just to the left of the default mask position."""
    y_shift: float
    """y_shift (float): Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For example, 1.0 will place the mask just below the default mask position."""
    scale: float
    """scale (float): Mask scaling coefficient. For example, 2.0 means double size."""


class InputSticker(BaseModel):
    """This object describes a sticker to be added to a sticker set.

    https://core.telegram.org/bots/api/#inputsticker
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    sticker: Union["InputFile", str]
    """sticker (Union["InputFile", str]): The added sticker. Pass a *file_id* as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, upload a new one using multipart/form-data, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. Animated and video stickers can't be uploaded via HTTP URL. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)"""
    format_: str
    """format_ (str): Format of the added sticker, must be one of “static” for a **.WEBP** or **.PNG** image, “animated” for a **.TGS** animation, “video” for a **.WEBM** video"""
    emoji_list: List[str]
    """emoji_list (List[str]): List of 1-20 emoji associated with the sticker"""
    mask_position: Optional["MaskPosition"] = None
    """mask_position ("MaskPosition"): *Optional*. Position where the mask should be placed on faces. For “mask” stickers only."""
    keywords: Optional[List[str]] = None
    """keywords (List[str]): *Optional*. List of 0-20 search keywords for the sticker with total length of up to 64 characters. For “regular” and “custom_emoji” stickers only."""


class Gift(BaseModel):
    """This object represents a gift that can be sent by the bot.

    https://core.telegram.org/bots/api/#gift
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    id: str
    """id (str): Unique identifier of the gift"""
    sticker: "Sticker"
    """sticker ("Sticker"): The sticker that represents the gift"""
    star_count: int
    """star_count (int): The number of Telegram Stars that must be paid to send the sticker"""
    upgrade_star_count: Optional[int] = None
    """upgrade_star_count (int): *Optional*. The number of Telegram Stars that must be paid to upgrade the gift to a unique one"""
    total_count: Optional[int] = None
    """total_count (int): *Optional*. The total number of the gifts of this type that can be sent; for limited gifts only"""
    remaining_count: Optional[int] = None
    """remaining_count (int): *Optional*. The number of remaining gifts of this type that can be sent; for limited gifts only"""


class Gifts(BaseModel):
    """This object represent a list of gifts.

    https://core.telegram.org/bots/api/#gifts
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    gifts: List["Gift"]
    """gifts (List["Gift"]): The list of gifts"""


class InlineQuery(BaseModel):
    """This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.

    https://core.telegram.org/bots/api/#inlinequery
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    id: str
    """id (str): Unique identifier for this query"""
    from_: "User"
    """from_ ("User"): Sender"""
    query: str
    """query (str): Text of the query (up to 256 characters)"""
    offset: str
    """offset (str): Offset of the results to be returned, can be controlled by the bot"""
    chat_type: Optional[str] = None
    """chat_type (str): *Optional*. Type of the chat from which the inline query was sent. Can be either “sender” for a private chat with the inline query sender, “private”, “group”, “supergroup”, or “channel”. The chat type should be always known for requests sent from official clients and most third-party clients, unless the request was sent from a secret chat"""
    location: Optional["Location"] = None
    """location ("Location"): *Optional*. Sender location, only for bots that request user location"""


class InlineQueryResultsButton(BaseModel):
    """This object represents a button to be shown above inline query results. You **must** use exactly one of the optional fields.

    https://core.telegram.org/bots/api/#inlinequeryresultsbutton
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    text: str
    """text (str): Label text on the button"""
    web_app: Optional["WebAppInfo"] = None
    """web_app ("WebAppInfo"): *Optional*. Description of the [Web App](https://core.telegram.org/bots/webapps) that will be launched when the user presses the button. The Web App will be able to switch back to the inline mode using the method [switchInlineQuery](https://core.telegram.org/bots/webapps#initializing-mini-apps) inside the Web App."""
    start_parameter: Optional[str] = None
    """start_parameter (str): *Optional*. [Deep-linking](https://core.telegram.org/bots/features#deep-linking) parameter for the /start message sent to the bot when a user presses the button. 1-64 characters, only `A-Z`, `a-z`, `0-9`, `_` and `-` are allowed.  

*Example:* An inline bot that sends YouTube videos can ask the user to connect the bot to their YouTube account to adapt search results accordingly. To do this, it displays a 'Connect your YouTube account' button above the results, or even before showing any. The user presses the button, switches to a private chat with the bot and, in doing so, passes a start parameter that instructs the bot to return an OAuth link. Once done, the bot can offer a [*switch_inline*](https://core.telegram.org/bots/api/#inlinekeyboardmarkup) button so that the user can easily return to the chat where they wanted to use the bot's inline capabilities."""


InlineQueryResult = Union["InlineQueryResultCachedAudio", "InlineQueryResultCachedDocument", "InlineQueryResultCachedGif", "InlineQueryResultCachedMpeg4Gif", "InlineQueryResultCachedPhoto", "InlineQueryResultCachedSticker", "InlineQueryResultCachedVideo", "InlineQueryResultCachedVoice", "InlineQueryResultArticle",
                          "InlineQueryResultAudio", "InlineQueryResultContact", "InlineQueryResultGame", "InlineQueryResultDocument", "InlineQueryResultGif", "InlineQueryResultLocation", "InlineQueryResultMpeg4Gif", "InlineQueryResultPhoto", "InlineQueryResultVenue", "InlineQueryResultVideo", "InlineQueryResultVoice"]
"""This object represents one result of an inline query. Telegram clients currently support results of the following 20 types:

* [InlineQueryResultCachedAudio](https://core.telegram.org/bots/api/#inlinequeryresultcachedaudio)
* [InlineQueryResultCachedDocument](https://core.telegram.org/bots/api/#inlinequeryresultcacheddocument)
* [InlineQueryResultCachedGif](https://core.telegram.org/bots/api/#inlinequeryresultcachedgif)
* [InlineQueryResultCachedMpeg4Gif](https://core.telegram.org/bots/api/#inlinequeryresultcachedmpeg4gif)
* [InlineQueryResultCachedPhoto](https://core.telegram.org/bots/api/#inlinequeryresultcachedphoto)
* [InlineQueryResultCachedSticker](https://core.telegram.org/bots/api/#inlinequeryresultcachedsticker)
* [InlineQueryResultCachedVideo](https://core.telegram.org/bots/api/#inlinequeryresultcachedvideo)
* [InlineQueryResultCachedVoice](https://core.telegram.org/bots/api/#inlinequeryresultcachedvoice)
* [InlineQueryResultArticle](https://core.telegram.org/bots/api/#inlinequeryresultarticle)
* [InlineQueryResultAudio](https://core.telegram.org/bots/api/#inlinequeryresultaudio)
* [InlineQueryResultContact](https://core.telegram.org/bots/api/#inlinequeryresultcontact)
* [InlineQueryResultGame](https://core.telegram.org/bots/api/#inlinequeryresultgame)
* [InlineQueryResultDocument](https://core.telegram.org/bots/api/#inlinequeryresultdocument)
* [InlineQueryResultGif](https://core.telegram.org/bots/api/#inlinequeryresultgif)
* [InlineQueryResultLocation](https://core.telegram.org/bots/api/#inlinequeryresultlocation)
* [InlineQueryResultMpeg4Gif](https://core.telegram.org/bots/api/#inlinequeryresultmpeg4gif)
* [InlineQueryResultPhoto](https://core.telegram.org/bots/api/#inlinequeryresultphoto)
* [InlineQueryResultVenue](https://core.telegram.org/bots/api/#inlinequeryresultvenue)
* [InlineQueryResultVideo](https://core.telegram.org/bots/api/#inlinequeryresultvideo)
* [InlineQueryResultVoice](https://core.telegram.org/bots/api/#inlinequeryresultvoice)"""


class InlineQueryResultArticle(BaseModel):
    """Represents a link to an article or web page.

    https://core.telegram.org/bots/api/#inlinequeryresultarticle
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "article"
    """type_ (str): Type of the result, must be *article*"""
    id: str
    """id (str): Unique identifier for this result, 1-64 Bytes"""
    title: str
    """title (str): Title of the result"""
    input_message_content: "InputMessageContent"
    """input_message_content ("InputMessageContent"): Content of the message to be sent"""
    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """reply_markup ("InlineKeyboardMarkup"): *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message"""
    url: Optional[str] = None
    """url (str): *Optional*. URL of the result"""
    description: Optional[str] = None
    """description (str): *Optional*. Short description of the result"""
    thumbnail_url: Optional[str] = None
    """thumbnail_url (str): *Optional*. Url of the thumbnail for the result"""
    thumbnail_width: Optional[int] = None
    """thumbnail_width (int): *Optional*. Thumbnail width"""
    thumbnail_height: Optional[int] = None
    """thumbnail_height (int): *Optional*. Thumbnail height"""


class InlineQueryResultPhoto(BaseModel):
    """Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the photo.

    https://core.telegram.org/bots/api/#inlinequeryresultphoto
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "photo"
    """type_ (str): Type of the result, must be *photo*"""
    id: str
    """id (str): Unique identifier for this result, 1-64 bytes"""
    photo_url: str
    """photo_url (str): A valid URL of the photo. Photo must be in **JPEG** format. Photo size must not exceed 5MB"""
    thumbnail_url: str
    """thumbnail_url (str): URL of the thumbnail for the photo"""
    photo_width: Optional[int] = None
    """photo_width (int): *Optional*. Width of the photo"""
    photo_height: Optional[int] = None
    """photo_height (int): *Optional*. Height of the photo"""
    title: Optional[str] = None
    """title (str): *Optional*. Title for the result"""
    description: Optional[str] = None
    """description (str): *Optional*. Short description of the result"""
    caption: Optional[str] = None
    """caption (str): *Optional*. Caption of the photo to be sent, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = None
    """parse_mode (str): *Optional*. Mode for parsing entities in the photo caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details."""
    caption_entities: Optional[List["MessageEntity"]] = None
    """caption_entities (List["MessageEntity"]): *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*"""
    show_caption_above_media: Optional[bool] = None
    """show_caption_above_media (bool): *Optional*. Pass *True*, if the caption must be shown above the message media"""
    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """reply_markup ("InlineKeyboardMarkup"): *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message"""
    input_message_content: Optional["InputMessageContent"] = None
    """input_message_content ("InputMessageContent"): *Optional*. Content of the message to be sent instead of the photo"""


class InlineQueryResultGif(BaseModel):
    """Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api/#inlinequeryresultgif
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "gif"
    """type_ (str): Type of the result, must be *gif*"""
    id: str
    """id (str): Unique identifier for this result, 1-64 bytes"""
    gif_url: str
    """gif_url (str): A valid URL for the GIF file"""
    gif_width: Optional[int] = None
    """gif_width (int): *Optional*. Width of the GIF"""
    gif_height: Optional[int] = None
    """gif_height (int): *Optional*. Height of the GIF"""
    gif_duration: Optional[int] = None
    """gif_duration (int): *Optional*. Duration of the GIF in seconds"""
    thumbnail_url: str
    """thumbnail_url (str): URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result"""
    thumbnail_mime_type: Optional[str] = "image/jpeg"
    """thumbnail_mime_type (str): *Optional*. MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg”"""
    title: Optional[str] = None
    """title (str): *Optional*. Title for the result"""
    caption: Optional[str] = None
    """caption (str): *Optional*. Caption of the GIF file to be sent, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = None
    """parse_mode (str): *Optional*. Mode for parsing entities in the caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details."""
    caption_entities: Optional[List["MessageEntity"]] = None
    """caption_entities (List["MessageEntity"]): *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*"""
    show_caption_above_media: Optional[bool] = None
    """show_caption_above_media (bool): *Optional*. Pass *True*, if the caption must be shown above the message media"""
    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """reply_markup ("InlineKeyboardMarkup"): *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message"""
    input_message_content: Optional["InputMessageContent"] = None
    """input_message_content ("InputMessageContent"): *Optional*. Content of the message to be sent instead of the GIF animation"""


class InlineQueryResultMpeg4Gif(BaseModel):
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api/#inlinequeryresultmpeg4gif
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "mpeg4_gif"
    """type_ (str): Type of the result, must be *mpeg4_gif*"""
    id: str
    """id (str): Unique identifier for this result, 1-64 bytes"""
    mpeg4_url: str
    """mpeg4_url (str): A valid URL for the MPEG4 file"""
    mpeg4_width: Optional[int] = None
    """mpeg4_width (int): *Optional*. Video width"""
    mpeg4_height: Optional[int] = None
    """mpeg4_height (int): *Optional*. Video height"""
    mpeg4_duration: Optional[int] = None
    """mpeg4_duration (int): *Optional*. Video duration in seconds"""
    thumbnail_url: str
    """thumbnail_url (str): URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result"""
    thumbnail_mime_type: Optional[str] = "image/jpeg"
    """thumbnail_mime_type (str): *Optional*. MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg”"""
    title: Optional[str] = None
    """title (str): *Optional*. Title for the result"""
    caption: Optional[str] = None
    """caption (str): *Optional*. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = None
    """parse_mode (str): *Optional*. Mode for parsing entities in the caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details."""
    caption_entities: Optional[List["MessageEntity"]] = None
    """caption_entities (List["MessageEntity"]): *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*"""
    show_caption_above_media: Optional[bool] = None
    """show_caption_above_media (bool): *Optional*. Pass *True*, if the caption must be shown above the message media"""
    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """reply_markup ("InlineKeyboardMarkup"): *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message"""
    input_message_content: Optional["InputMessageContent"] = None
    """input_message_content ("InputMessageContent"): *Optional*. Content of the message to be sent instead of the video animation"""


class InlineQueryResultVideo(BaseModel):
    """Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the video.

If an InlineQueryResultVideo message contains an embedded video (e.g., YouTube), you **must** replace its content using *input_message_content*.

    https://core.telegram.org/bots/api/#inlinequeryresultvideo
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "video"
    """type_ (str): Type of the result, must be *video*"""
    id: str
    """id (str): Unique identifier for this result, 1-64 bytes"""
    video_url: str
    """video_url (str): A valid URL for the embedded video player or video file"""
    mime_type: str
    """mime_type (str): MIME type of the content of the video URL, “text/html” or “video/mp4”"""
    thumbnail_url: str
    """thumbnail_url (str): URL of the thumbnail (JPEG only) for the video"""
    title: str
    """title (str): Title for the result"""
    caption: Optional[str] = None
    """caption (str): *Optional*. Caption of the video to be sent, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = None
    """parse_mode (str): *Optional*. Mode for parsing entities in the video caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details."""
    caption_entities: Optional[List["MessageEntity"]] = None
    """caption_entities (List["MessageEntity"]): *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*"""
    show_caption_above_media: Optional[bool] = None
    """show_caption_above_media (bool): *Optional*. Pass *True*, if the caption must be shown above the message media"""
    video_width: Optional[int] = None
    """video_width (int): *Optional*. Video width"""
    video_height: Optional[int] = None
    """video_height (int): *Optional*. Video height"""
    video_duration: Optional[int] = None
    """video_duration (int): *Optional*. Video duration in seconds"""
    description: Optional[str] = None
    """description (str): *Optional*. Short description of the result"""
    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """reply_markup ("InlineKeyboardMarkup"): *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message"""
    input_message_content: Optional["InputMessageContent"] = None
    """input_message_content ("InputMessageContent"): *Optional*. Content of the message to be sent instead of the video. This field is **required** if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a YouTube video)."""


class InlineQueryResultAudio(BaseModel):
    """Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the audio.

    https://core.telegram.org/bots/api/#inlinequeryresultaudio
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "audio"
    """type_ (str): Type of the result, must be *audio*"""
    id: str
    """id (str): Unique identifier for this result, 1-64 bytes"""
    audio_url: str
    """audio_url (str): A valid URL for the audio file"""
    title: str
    """title (str): Title"""
    caption: Optional[str] = None
    """caption (str): *Optional*. Caption, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = None
    """parse_mode (str): *Optional*. Mode for parsing entities in the audio caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details."""
    caption_entities: Optional[List["MessageEntity"]] = None
    """caption_entities (List["MessageEntity"]): *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*"""
    performer: Optional[str] = None
    """performer (str): *Optional*. Performer"""
    audio_duration: Optional[int] = None
    """audio_duration (int): *Optional*. Audio duration in seconds"""
    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """reply_markup ("InlineKeyboardMarkup"): *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message"""
    input_message_content: Optional["InputMessageContent"] = None
    """input_message_content ("InputMessageContent"): *Optional*. Content of the message to be sent instead of the audio"""


class InlineQueryResultVoice(BaseModel):
    """Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the the voice message.

    https://core.telegram.org/bots/api/#inlinequeryresultvoice
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "voice"
    """type_ (str): Type of the result, must be *voice*"""
    id: str
    """id (str): Unique identifier for this result, 1-64 bytes"""
    voice_url: str
    """voice_url (str): A valid URL for the voice recording"""
    title: str
    """title (str): Recording title"""
    caption: Optional[str] = None
    """caption (str): *Optional*. Caption, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = None
    """parse_mode (str): *Optional*. Mode for parsing entities in the voice message caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details."""
    caption_entities: Optional[List["MessageEntity"]] = None
    """caption_entities (List["MessageEntity"]): *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*"""
    voice_duration: Optional[int] = None
    """voice_duration (int): *Optional*. Recording duration in seconds"""
    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """reply_markup ("InlineKeyboardMarkup"): *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message"""
    input_message_content: Optional["InputMessageContent"] = None
    """input_message_content ("InputMessageContent"): *Optional*. Content of the message to be sent instead of the voice recording"""


class InlineQueryResultDocument(BaseModel):
    """Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the file. Currently, only **.PDF** and **.ZIP** files can be sent using this method.

    https://core.telegram.org/bots/api/#inlinequeryresultdocument
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "document"
    """type_ (str): Type of the result, must be *document*"""
    id: str
    """id (str): Unique identifier for this result, 1-64 bytes"""
    title: str
    """title (str): Title for the result"""
    caption: Optional[str] = None
    """caption (str): *Optional*. Caption of the document to be sent, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = None
    """parse_mode (str): *Optional*. Mode for parsing entities in the document caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details."""
    caption_entities: Optional[List["MessageEntity"]] = None
    """caption_entities (List["MessageEntity"]): *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*"""
    document_url: str
    """document_url (str): A valid URL for the file"""
    mime_type: str
    """mime_type (str): MIME type of the content of the file, either “application/pdf” or “application/zip”"""
    description: Optional[str] = None
    """description (str): *Optional*. Short description of the result"""
    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """reply_markup ("InlineKeyboardMarkup"): *Optional*. Inline keyboard attached to the message"""
    input_message_content: Optional["InputMessageContent"] = None
    """input_message_content ("InputMessageContent"): *Optional*. Content of the message to be sent instead of the file"""
    thumbnail_url: Optional[str] = None
    """thumbnail_url (str): *Optional*. URL of the thumbnail (JPEG only) for the file"""
    thumbnail_width: Optional[int] = None
    """thumbnail_width (int): *Optional*. Thumbnail width"""
    thumbnail_height: Optional[int] = None
    """thumbnail_height (int): *Optional*. Thumbnail height"""


class InlineQueryResultLocation(BaseModel):
    """Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the location.

    https://core.telegram.org/bots/api/#inlinequeryresultlocation
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "location"
    """type_ (str): Type of the result, must be *location*"""
    id: str
    """id (str): Unique identifier for this result, 1-64 Bytes"""
    latitude: float
    """latitude (float): Location latitude in degrees"""
    longitude: float
    """longitude (float): Location longitude in degrees"""
    title: str
    """title (str): Location title"""
    horizontal_accuracy: Optional[float] = None
    """horizontal_accuracy (float): *Optional*. The radius of uncertainty for the location, measured in meters; 0-1500"""
    live_period: Optional[int] = None
    """live_period (int): *Optional*. Period in seconds during which the location can be updated, should be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely."""
    heading: Optional[int] = None
    """heading (int): *Optional*. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified."""
    proximity_alert_radius: Optional[int] = None
    """proximity_alert_radius (int): *Optional*. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified."""
    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """reply_markup ("InlineKeyboardMarkup"): *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message"""
    input_message_content: Optional["InputMessageContent"] = None
    """input_message_content ("InputMessageContent"): *Optional*. Content of the message to be sent instead of the location"""
    thumbnail_url: Optional[str] = None
    """thumbnail_url (str): *Optional*. Url of the thumbnail for the result"""
    thumbnail_width: Optional[int] = None
    """thumbnail_width (int): *Optional*. Thumbnail width"""
    thumbnail_height: Optional[int] = None
    """thumbnail_height (int): *Optional*. Thumbnail height"""


class InlineQueryResultVenue(BaseModel):
    """Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the venue.

    https://core.telegram.org/bots/api/#inlinequeryresultvenue
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "venue"
    """type_ (str): Type of the result, must be *venue*"""
    id: str
    """id (str): Unique identifier for this result, 1-64 Bytes"""
    latitude: float
    """latitude (float): Latitude of the venue location in degrees"""
    longitude: float
    """longitude (float): Longitude of the venue location in degrees"""
    title: str
    """title (str): Title of the venue"""
    address: str
    """address (str): Address of the venue"""
    foursquare_id: Optional[str] = None
    """foursquare_id (str): *Optional*. Foursquare identifier of the venue if known"""
    foursquare_type: Optional[str] = None
    """foursquare_type (str): *Optional*. Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)"""
    google_place_id: Optional[str] = None
    """google_place_id (str): *Optional*. Google Places identifier of the venue"""
    google_place_type: Optional[str] = None
    """google_place_type (str): *Optional*. Google Places type of the venue. (See [supported types](https://developers.google.com/places/web-service/supported_types).)"""
    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """reply_markup ("InlineKeyboardMarkup"): *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message"""
    input_message_content: Optional["InputMessageContent"] = None
    """input_message_content ("InputMessageContent"): *Optional*. Content of the message to be sent instead of the venue"""
    thumbnail_url: Optional[str] = None
    """thumbnail_url (str): *Optional*. Url of the thumbnail for the result"""
    thumbnail_width: Optional[int] = None
    """thumbnail_width (int): *Optional*. Thumbnail width"""
    thumbnail_height: Optional[int] = None
    """thumbnail_height (int): *Optional*. Thumbnail height"""


class InlineQueryResultContact(BaseModel):
    """Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the contact.

    https://core.telegram.org/bots/api/#inlinequeryresultcontact
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "contact"
    """type_ (str): Type of the result, must be *contact*"""
    id: str
    """id (str): Unique identifier for this result, 1-64 Bytes"""
    phone_number: str
    """phone_number (str): Contact's phone number"""
    first_name: str
    """first_name (str): Contact's first name"""
    last_name: Optional[str] = None
    """last_name (str): *Optional*. Contact's last name"""
    vcard: Optional[str] = None
    """vcard (str): *Optional*. Additional data about the contact in the form of a [vCard](https://en.wikipedia.org/wiki/VCard), 0-2048 bytes"""
    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """reply_markup ("InlineKeyboardMarkup"): *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message"""
    input_message_content: Optional["InputMessageContent"] = None
    """input_message_content ("InputMessageContent"): *Optional*. Content of the message to be sent instead of the contact"""
    thumbnail_url: Optional[str] = None
    """thumbnail_url (str): *Optional*. Url of the thumbnail for the result"""
    thumbnail_width: Optional[int] = None
    """thumbnail_width (int): *Optional*. Thumbnail width"""
    thumbnail_height: Optional[int] = None
    """thumbnail_height (int): *Optional*. Thumbnail height"""


class InlineQueryResultGame(BaseModel):
    """Represents a [Game](https://core.telegram.org/bots/api/#games).

    https://core.telegram.org/bots/api/#inlinequeryresultgame
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "game"
    """type_ (str): Type of the result, must be *game*"""
    id: str
    """id (str): Unique identifier for this result, 1-64 bytes"""
    game_short_name: str
    """game_short_name (str): Short name of the game"""
    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """reply_markup ("InlineKeyboardMarkup"): *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message"""


class InlineQueryResultCachedPhoto(BaseModel):
    """Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the photo.

    https://core.telegram.org/bots/api/#inlinequeryresultcachedphoto
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "photo"
    """type_ (str): Type of the result, must be *photo*"""
    id: str
    """id (str): Unique identifier for this result, 1-64 bytes"""
    photo_file_id: str
    """photo_file_id (str): A valid file identifier of the photo"""
    title: Optional[str] = None
    """title (str): *Optional*. Title for the result"""
    description: Optional[str] = None
    """description (str): *Optional*. Short description of the result"""
    caption: Optional[str] = None
    """caption (str): *Optional*. Caption of the photo to be sent, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = None
    """parse_mode (str): *Optional*. Mode for parsing entities in the photo caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details."""
    caption_entities: Optional[List["MessageEntity"]] = None
    """caption_entities (List["MessageEntity"]): *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*"""
    show_caption_above_media: Optional[bool] = None
    """show_caption_above_media (bool): *Optional*. Pass *True*, if the caption must be shown above the message media"""
    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """reply_markup ("InlineKeyboardMarkup"): *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message"""
    input_message_content: Optional["InputMessageContent"] = None
    """input_message_content ("InputMessageContent"): *Optional*. Content of the message to be sent instead of the photo"""


class InlineQueryResultCachedGif(BaseModel):
    """Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use *input_message_content* to send a message with specified content instead of the animation.

    https://core.telegram.org/bots/api/#inlinequeryresultcachedgif
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "gif"
    """type_ (str): Type of the result, must be *gif*"""
    id: str
    """id (str): Unique identifier for this result, 1-64 bytes"""
    gif_file_id: str
    """gif_file_id (str): A valid file identifier for the GIF file"""
    title: Optional[str] = None
    """title (str): *Optional*. Title for the result"""
    caption: Optional[str] = None
    """caption (str): *Optional*. Caption of the GIF file to be sent, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = None
    """parse_mode (str): *Optional*. Mode for parsing entities in the caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details."""
    caption_entities: Optional[List["MessageEntity"]] = None
    """caption_entities (List["MessageEntity"]): *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*"""
    show_caption_above_media: Optional[bool] = None
    """show_caption_above_media (bool): *Optional*. Pass *True*, if the caption must be shown above the message media"""
    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """reply_markup ("InlineKeyboardMarkup"): *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message"""
    input_message_content: Optional["InputMessageContent"] = None
    """input_message_content ("InputMessageContent"): *Optional*. Content of the message to be sent instead of the GIF animation"""


class InlineQueryResultCachedMpeg4Gif(BaseModel):
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api/#inlinequeryresultcachedmpeg4gif
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "mpeg4_gif"
    """type_ (str): Type of the result, must be *mpeg4_gif*"""
    id: str
    """id (str): Unique identifier for this result, 1-64 bytes"""
    mpeg4_file_id: str
    """mpeg4_file_id (str): A valid file identifier for the MPEG4 file"""
    title: Optional[str] = None
    """title (str): *Optional*. Title for the result"""
    caption: Optional[str] = None
    """caption (str): *Optional*. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = None
    """parse_mode (str): *Optional*. Mode for parsing entities in the caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details."""
    caption_entities: Optional[List["MessageEntity"]] = None
    """caption_entities (List["MessageEntity"]): *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*"""
    show_caption_above_media: Optional[bool] = None
    """show_caption_above_media (bool): *Optional*. Pass *True*, if the caption must be shown above the message media"""
    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """reply_markup ("InlineKeyboardMarkup"): *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message"""
    input_message_content: Optional["InputMessageContent"] = None
    """input_message_content ("InputMessageContent"): *Optional*. Content of the message to be sent instead of the video animation"""


class InlineQueryResultCachedSticker(BaseModel):
    """Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the sticker.

    https://core.telegram.org/bots/api/#inlinequeryresultcachedsticker
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "sticker"
    """type_ (str): Type of the result, must be *sticker*"""
    id: str
    """id (str): Unique identifier for this result, 1-64 bytes"""
    sticker_file_id: str
    """sticker_file_id (str): A valid file identifier of the sticker"""
    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """reply_markup ("InlineKeyboardMarkup"): *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message"""
    input_message_content: Optional["InputMessageContent"] = None
    """input_message_content ("InputMessageContent"): *Optional*. Content of the message to be sent instead of the sticker"""


class InlineQueryResultCachedDocument(BaseModel):
    """Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the file.

    https://core.telegram.org/bots/api/#inlinequeryresultcacheddocument
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "document"
    """type_ (str): Type of the result, must be *document*"""
    id: str
    """id (str): Unique identifier for this result, 1-64 bytes"""
    title: str
    """title (str): Title for the result"""
    document_file_id: str
    """document_file_id (str): A valid file identifier for the file"""
    description: Optional[str] = None
    """description (str): *Optional*. Short description of the result"""
    caption: Optional[str] = None
    """caption (str): *Optional*. Caption of the document to be sent, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = None
    """parse_mode (str): *Optional*. Mode for parsing entities in the document caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details."""
    caption_entities: Optional[List["MessageEntity"]] = None
    """caption_entities (List["MessageEntity"]): *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*"""
    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """reply_markup ("InlineKeyboardMarkup"): *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message"""
    input_message_content: Optional["InputMessageContent"] = None
    """input_message_content ("InputMessageContent"): *Optional*. Content of the message to be sent instead of the file"""


class InlineQueryResultCachedVideo(BaseModel):
    """Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the video.

    https://core.telegram.org/bots/api/#inlinequeryresultcachedvideo
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "video"
    """type_ (str): Type of the result, must be *video*"""
    id: str
    """id (str): Unique identifier for this result, 1-64 bytes"""
    video_file_id: str
    """video_file_id (str): A valid file identifier for the video file"""
    title: str
    """title (str): Title for the result"""
    description: Optional[str] = None
    """description (str): *Optional*. Short description of the result"""
    caption: Optional[str] = None
    """caption (str): *Optional*. Caption of the video to be sent, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = None
    """parse_mode (str): *Optional*. Mode for parsing entities in the video caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details."""
    caption_entities: Optional[List["MessageEntity"]] = None
    """caption_entities (List["MessageEntity"]): *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*"""
    show_caption_above_media: Optional[bool] = None
    """show_caption_above_media (bool): *Optional*. Pass *True*, if the caption must be shown above the message media"""
    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """reply_markup ("InlineKeyboardMarkup"): *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message"""
    input_message_content: Optional["InputMessageContent"] = None
    """input_message_content ("InputMessageContent"): *Optional*. Content of the message to be sent instead of the video"""


class InlineQueryResultCachedVoice(BaseModel):
    """Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the voice message.

    https://core.telegram.org/bots/api/#inlinequeryresultcachedvoice
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "voice"
    """type_ (str): Type of the result, must be *voice*"""
    id: str
    """id (str): Unique identifier for this result, 1-64 bytes"""
    voice_file_id: str
    """voice_file_id (str): A valid file identifier for the voice message"""
    title: str
    """title (str): Voice message title"""
    caption: Optional[str] = None
    """caption (str): *Optional*. Caption, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = None
    """parse_mode (str): *Optional*. Mode for parsing entities in the voice message caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details."""
    caption_entities: Optional[List["MessageEntity"]] = None
    """caption_entities (List["MessageEntity"]): *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*"""
    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """reply_markup ("InlineKeyboardMarkup"): *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message"""
    input_message_content: Optional["InputMessageContent"] = None
    """input_message_content ("InputMessageContent"): *Optional*. Content of the message to be sent instead of the voice message"""


class InlineQueryResultCachedAudio(BaseModel):
    """Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the audio.

    https://core.telegram.org/bots/api/#inlinequeryresultcachedaudio
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "audio"
    """type_ (str): Type of the result, must be *audio*"""
    id: str
    """id (str): Unique identifier for this result, 1-64 bytes"""
    audio_file_id: str
    """audio_file_id (str): A valid file identifier for the audio file"""
    caption: Optional[str] = None
    """caption (str): *Optional*. Caption, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = None
    """parse_mode (str): *Optional*. Mode for parsing entities in the audio caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details."""
    caption_entities: Optional[List["MessageEntity"]] = None
    """caption_entities (List["MessageEntity"]): *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*"""
    reply_markup: Optional["InlineKeyboardMarkup"] = None
    """reply_markup ("InlineKeyboardMarkup"): *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message"""
    input_message_content: Optional["InputMessageContent"] = None
    """input_message_content ("InputMessageContent"): *Optional*. Content of the message to be sent instead of the audio"""


InputMessageContent = Union["InputTextMessageContent", "InputLocationMessageContent",
                            "InputVenueMessageContent", "InputContactMessageContent", "InputInvoiceMessageContent"]
"""This object represents the content of a message to be sent as a result of an inline query. Telegram clients currently support the following 5 types:

* [InputTextMessageContent](https://core.telegram.org/bots/api/#inputtextmessagecontent)
* [InputLocationMessageContent](https://core.telegram.org/bots/api/#inputlocationmessagecontent)
* [InputVenueMessageContent](https://core.telegram.org/bots/api/#inputvenuemessagecontent)
* [InputContactMessageContent](https://core.telegram.org/bots/api/#inputcontactmessagecontent)
* [InputInvoiceMessageContent](https://core.telegram.org/bots/api/#inputinvoicemessagecontent)"""


class InputTextMessageContent(BaseModel):
    """Represents the [content](https://core.telegram.org/bots/api/#inputmessagecontent) of a text message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api/#inputtextmessagecontent
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    message_text: str
    """message_text (str): Text of the message to be sent, 1-4096 characters"""
    parse_mode: Optional[str] = None
    """parse_mode (str): *Optional*. Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details."""
    entities: Optional[List["MessageEntity"]] = None
    """entities (List["MessageEntity"]): *Optional*. List of special entities that appear in message text, which can be specified instead of *parse_mode*"""
    link_preview_options: Optional["LinkPreviewOptions"] = None
    """link_preview_options ("LinkPreviewOptions"): *Optional*. Link preview generation options for the message"""


class InputLocationMessageContent(BaseModel):
    """Represents the [content](https://core.telegram.org/bots/api/#inputmessagecontent) of a location message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api/#inputlocationmessagecontent
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    latitude: float
    """latitude (float): Latitude of the location in degrees"""
    longitude: float
    """longitude (float): Longitude of the location in degrees"""
    horizontal_accuracy: Optional[float] = None
    """horizontal_accuracy (float): *Optional*. The radius of uncertainty for the location, measured in meters; 0-1500"""
    live_period: Optional[int] = None
    """live_period (int): *Optional*. Period in seconds during which the location can be updated, should be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely."""
    heading: Optional[int] = None
    """heading (int): *Optional*. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified."""
    proximity_alert_radius: Optional[int] = None
    """proximity_alert_radius (int): *Optional*. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified."""


class InputVenueMessageContent(BaseModel):
    """Represents the [content](https://core.telegram.org/bots/api/#inputmessagecontent) of a venue message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api/#inputvenuemessagecontent
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    latitude: float
    """latitude (float): Latitude of the venue in degrees"""
    longitude: float
    """longitude (float): Longitude of the venue in degrees"""
    title: str
    """title (str): Name of the venue"""
    address: str
    """address (str): Address of the venue"""
    foursquare_id: Optional[str] = None
    """foursquare_id (str): *Optional*. Foursquare identifier of the venue, if known"""
    foursquare_type: Optional[str] = None
    """foursquare_type (str): *Optional*. Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)"""
    google_place_id: Optional[str] = None
    """google_place_id (str): *Optional*. Google Places identifier of the venue"""
    google_place_type: Optional[str] = None
    """google_place_type (str): *Optional*. Google Places type of the venue. (See [supported types](https://developers.google.com/places/web-service/supported_types).)"""


class InputContactMessageContent(BaseModel):
    """Represents the [content](https://core.telegram.org/bots/api/#inputmessagecontent) of a contact message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api/#inputcontactmessagecontent
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    phone_number: str
    """phone_number (str): Contact's phone number"""
    first_name: str
    """first_name (str): Contact's first name"""
    last_name: Optional[str] = None
    """last_name (str): *Optional*. Contact's last name"""
    vcard: Optional[str] = None
    """vcard (str): *Optional*. Additional data about the contact in the form of a [vCard](https://en.wikipedia.org/wiki/VCard), 0-2048 bytes"""


class InputInvoiceMessageContent(BaseModel):
    """Represents the [content](https://core.telegram.org/bots/api/#inputmessagecontent) of an invoice message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api/#inputinvoicemessagecontent
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    title: str
    """title (str): Product name, 1-32 characters"""
    description: str
    """description (str): Product description, 1-255 characters"""
    payload: str
    """payload (str): Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use it for your internal processes."""
    provider_token: Optional[str] = None
    """provider_token (str): *Optional*. Payment provider token, obtained via [@BotFather](https://t.me/botfather). Pass an empty string for payments in [Telegram Stars](https://t.me/BotNews/90)."""
    currency: str
    """currency (str): Three-letter ISO 4217 currency code, see [more on currencies](https://core.telegram.org/bots/payments#supported-currencies). Pass “XTR” for payments in [Telegram Stars](https://t.me/BotNews/90)."""
    prices: List["LabeledPrice"]
    """prices (List["LabeledPrice"]): Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in [Telegram Stars](https://t.me/BotNews/90)."""
    max_tip_amount: Optional[int] = None
    """max_tip_amount (int): *Optional*. The maximum accepted amount for tips in the *smallest units* of the currency (integer, **not** float/double). For example, for a maximum tip of `US$ 1.45` pass `max_tip_amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payments in [Telegram Stars](https://t.me/BotNews/90)."""
    suggested_tip_amounts: Optional[List[int]] = None
    """suggested_tip_amounts (List[int]): *Optional*. A JSON-serialized array of suggested amounts of tip in the *smallest units* of the currency (integer, **not** float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed *max_tip_amount*."""
    provider_data: Optional[str] = None
    """provider_data (str): *Optional*. A JSON-serialized object for data about the invoice, which will be shared with the payment provider. A detailed description of the required fields should be provided by the payment provider."""
    photo_url: Optional[str] = None
    """photo_url (str): *Optional*. URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service."""
    photo_size: Optional[int] = None
    """photo_size (int): *Optional*. Photo size in bytes"""
    photo_width: Optional[int] = None
    """photo_width (int): *Optional*. Photo width"""
    photo_height: Optional[int] = None
    """photo_height (int): *Optional*. Photo height"""
    need_name: Optional[bool] = None
    """need_name (bool): *Optional*. Pass *True* if you require the user's full name to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)."""
    need_phone_number: Optional[bool] = None
    """need_phone_number (bool): *Optional*. Pass *True* if you require the user's phone number to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)."""
    need_email: Optional[bool] = None
    """need_email (bool): *Optional*. Pass *True* if you require the user's email address to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)."""
    need_shipping_address: Optional[bool] = None
    """need_shipping_address (bool): *Optional*. Pass *True* if you require the user's shipping address to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)."""
    send_phone_number_to_provider: Optional[bool] = None
    """send_phone_number_to_provider (bool): *Optional*. Pass *True* if the user's phone number should be sent to the provider. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)."""
    send_email_to_provider: Optional[bool] = None
    """send_email_to_provider (bool): *Optional*. Pass *True* if the user's email address should be sent to the provider. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)."""
    is_flexible: Optional[bool] = None
    """is_flexible (bool): *Optional*. Pass *True* if the final price depends on the shipping method. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)."""


class ChosenInlineResult(BaseModel):
    """Represents a [result](https://core.telegram.org/bots/api/#inlinequeryresult) of an inline query that was chosen by the user and sent to their chat partner.

    https://core.telegram.org/bots/api/#choseninlineresult
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    result_id: str
    """result_id (str): The unique identifier for the result that was chosen"""
    from_: "User"
    """from_ ("User"): The user that chose the result"""
    location: Optional["Location"] = None
    """location ("Location"): *Optional*. Sender location, only for bots that require user location"""
    inline_message_id: Optional[str] = None
    """inline_message_id (str): *Optional*. Identifier of the sent inline message. Available only if there is an [inline keyboard](https://core.telegram.org/bots/api/#inlinekeyboardmarkup) attached to the message. Will be also received in [callback queries](https://core.telegram.org/bots/api/#callbackquery) and can be used to [edit](https://core.telegram.org/bots/api/#updating-messages) the message."""
    query: str
    """query (str): The query that was used to obtain the result"""


class SentWebAppMessage(BaseModel):
    """Describes an inline message sent by a [Web App](https://core.telegram.org/bots/webapps) on behalf of a user.

    https://core.telegram.org/bots/api/#sentwebappmessage
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    inline_message_id: Optional[str] = None
    """inline_message_id (str): *Optional*. Identifier of the sent inline message. Available only if there is an [inline keyboard](https://core.telegram.org/bots/api/#inlinekeyboardmarkup) attached to the message."""


class PreparedInlineMessage(BaseModel):
    """Describes an inline message to be sent by a user of a Mini App.

    https://core.telegram.org/bots/api/#preparedinlinemessage
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    id: str
    """id (str): Unique identifier of the prepared message"""
    expiration_date: int
    """expiration_date (int): Expiration date of the prepared message, in Unix time. Expired prepared messages can no longer be used"""


class LabeledPrice(BaseModel):
    """This object represents a portion of the price for goods or services.

    https://core.telegram.org/bots/api/#labeledprice
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    label: str
    """label (str): Portion label"""
    amount: int
    """amount (int): Price of the product in the *smallest units* of the [currency](https://core.telegram.org/bots/payments#supported-currencies) (integer, **not** float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies)."""


class Invoice(BaseModel):
    """This object contains basic information about an invoice.

    https://core.telegram.org/bots/api/#invoice
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    title: str
    """title (str): Product name"""
    description: str
    """description (str): Product description"""
    start_parameter: str
    """start_parameter (str): Unique bot deep-linking parameter that can be used to generate this invoice"""
    currency: str
    """currency (str): Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code, or “XTR” for payments in [Telegram Stars](https://t.me/BotNews/90)"""
    total_amount: int
    """total_amount (int): Total price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies)."""


class ShippingAddress(BaseModel):
    """This object represents a shipping address.

    https://core.telegram.org/bots/api/#shippingaddress
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    country_code: str
    """country_code (str): Two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code"""
    state: str
    """state (str): State, if applicable"""
    city: str
    """city (str): City"""
    street_line1: str
    """street_line1 (str): First line for the address"""
    street_line2: str
    """street_line2 (str): Second line for the address"""
    post_code: str
    """post_code (str): Address post code"""


class OrderInfo(BaseModel):
    """This object represents information about an order.

    https://core.telegram.org/bots/api/#orderinfo
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    name: Optional[str] = None
    """name (str): *Optional*. User name"""
    phone_number: Optional[str] = None
    """phone_number (str): *Optional*. User's phone number"""
    email: Optional[str] = None
    """email (str): *Optional*. User email"""
    shipping_address: Optional["ShippingAddress"] = None
    """shipping_address ("ShippingAddress"): *Optional*. User shipping address"""


class ShippingOption(BaseModel):
    """This object represents one shipping option.

    https://core.telegram.org/bots/api/#shippingoption
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    id: str
    """id (str): Shipping option identifier"""
    title: str
    """title (str): Option title"""
    prices: List["LabeledPrice"]
    """prices (List["LabeledPrice"]): List of price portions"""


class SuccessfulPayment(BaseModel):
    """This object contains basic information about a successful payment. Note that if the buyer initiates a chargeback with the relevant payment provider following this transaction, the funds may be debited from your balance. This is outside of Telegram's control.

    https://core.telegram.org/bots/api/#successfulpayment
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    currency: str
    """currency (str): Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code, or “XTR” for payments in [Telegram Stars](https://t.me/BotNews/90)"""
    total_amount: int
    """total_amount (int): Total price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies)."""
    invoice_payload: str
    """invoice_payload (str): Bot-specified invoice payload"""
    subscription_expiration_date: Optional[int] = None
    """subscription_expiration_date (int): *Optional*. Expiration date of the subscription, in Unix time; for recurring payments only"""
    is_recurring: Optional[bool] = True
    """is_recurring (bool): *Optional*. True, if the payment is a recurring payment for a subscription"""
    is_first_recurring: Optional[bool] = True
    """is_first_recurring (bool): *Optional*. True, if the payment is the first payment for a subscription"""
    shipping_option_id: Optional[str] = None
    """shipping_option_id (str): *Optional*. Identifier of the shipping option chosen by the user"""
    order_info: Optional["OrderInfo"] = None
    """order_info ("OrderInfo"): *Optional*. Order information provided by the user"""
    telegram_payment_charge_id: str
    """telegram_payment_charge_id (str): Telegram payment identifier"""
    provider_payment_charge_id: str
    """provider_payment_charge_id (str): Provider payment identifier"""


class RefundedPayment(BaseModel):
    """This object contains basic information about a refunded payment.

    https://core.telegram.org/bots/api/#refundedpayment
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    currency: str = "XTR"
    """currency (str): Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code, or “XTR” for payments in [Telegram Stars](https://t.me/BotNews/90). Currently, always “XTR”"""
    total_amount: int
    """total_amount (int): Total refunded price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of `US$ 1.45`, `total_amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies)."""
    invoice_payload: str
    """invoice_payload (str): Bot-specified invoice payload"""
    telegram_payment_charge_id: str
    """telegram_payment_charge_id (str): Telegram payment identifier"""
    provider_payment_charge_id: Optional[str] = None
    """provider_payment_charge_id (str): *Optional*. Provider payment identifier"""


class ShippingQuery(BaseModel):
    """This object contains information about an incoming shipping query.

    https://core.telegram.org/bots/api/#shippingquery
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    id: str
    """id (str): Unique query identifier"""
    from_: "User"
    """from_ ("User"): User who sent the query"""
    invoice_payload: str
    """invoice_payload (str): Bot-specified invoice payload"""
    shipping_address: "ShippingAddress"
    """shipping_address ("ShippingAddress"): User specified shipping address"""


class PreCheckoutQuery(BaseModel):
    """This object contains information about an incoming pre-checkout query.

    https://core.telegram.org/bots/api/#precheckoutquery
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    id: str
    """id (str): Unique query identifier"""
    from_: "User"
    """from_ ("User"): User who sent the query"""
    currency: str
    """currency (str): Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code, or “XTR” for payments in [Telegram Stars](https://t.me/BotNews/90)"""
    total_amount: int
    """total_amount (int): Total price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies)."""
    invoice_payload: str
    """invoice_payload (str): Bot-specified invoice payload"""
    shipping_option_id: Optional[str] = None
    """shipping_option_id (str): *Optional*. Identifier of the shipping option chosen by the user"""
    order_info: Optional["OrderInfo"] = None
    """order_info ("OrderInfo"): *Optional*. Order information provided by the user"""


class PaidMediaPurchased(BaseModel):
    """This object contains information about a paid media purchase.

    https://core.telegram.org/bots/api/#paidmediapurchased
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    from_: "User"
    """from_ ("User"): User who purchased the media"""
    paid_media_payload: str
    """paid_media_payload (str): Bot-specified paid media payload"""


RevenueWithdrawalState = Union["RevenueWithdrawalStatePending",
                               "RevenueWithdrawalStateSucceeded", "RevenueWithdrawalStateFailed"]
"""This object describes the state of a revenue withdrawal operation. Currently, it can be one of

* [RevenueWithdrawalStatePending](https://core.telegram.org/bots/api/#revenuewithdrawalstatepending)
* [RevenueWithdrawalStateSucceeded](https://core.telegram.org/bots/api/#revenuewithdrawalstatesucceeded)
* [RevenueWithdrawalStateFailed](https://core.telegram.org/bots/api/#revenuewithdrawalstatefailed)"""


class RevenueWithdrawalStatePending(BaseModel):
    """The withdrawal is in progress.

    https://core.telegram.org/bots/api/#revenuewithdrawalstatepending
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "pending"
    """type_ (str): Type of the state, always “pending”"""


class RevenueWithdrawalStateSucceeded(BaseModel):
    """The withdrawal succeeded.

    https://core.telegram.org/bots/api/#revenuewithdrawalstatesucceeded
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "succeeded"
    """type_ (str): Type of the state, always “succeeded”"""
    date: int
    """date (int): Date the withdrawal was completed in Unix time"""
    url: str
    """url (str): An HTTPS URL that can be used to see transaction details"""


class RevenueWithdrawalStateFailed(BaseModel):
    """The withdrawal failed and the transaction was refunded.

    https://core.telegram.org/bots/api/#revenuewithdrawalstatefailed
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "failed"
    """type_ (str): Type of the state, always “failed”"""


class AffiliateInfo(BaseModel):
    """Contains information about the affiliate that received a commission via this transaction.

    https://core.telegram.org/bots/api/#affiliateinfo
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    affiliate_user: Optional["User"] = None
    """affiliate_user ("User"): *Optional*. The bot or the user that received an affiliate commission if it was received by a bot or a user"""
    affiliate_chat: Optional["Chat"] = None
    """affiliate_chat ("Chat"): *Optional*. The chat that received an affiliate commission if it was received by a chat"""
    commission_per_mille: int
    """commission_per_mille (int): The number of Telegram Stars received by the affiliate for each 1000 Telegram Stars received by the bot from referred users"""
    amount: int
    """amount (int): Integer amount of Telegram Stars received by the affiliate from the transaction, rounded to 0; can be negative for refunds"""
    nanostar_amount: Optional[int] = None
    """nanostar_amount (int): *Optional*. The number of 1/1000000000 shares of Telegram Stars received by the affiliate; from -999999999 to 999999999; can be negative for refunds"""


TransactionPartner = Union["TransactionPartnerUser", "TransactionPartnerChat", "TransactionPartnerAffiliateProgram",
                           "TransactionPartnerFragment", "TransactionPartnerTelegramAds", "TransactionPartnerTelegramApi", "TransactionPartnerOther"]
"""This object describes the source of a transaction, or its recipient for outgoing transactions. Currently, it can be one of

* [TransactionPartnerUser](https://core.telegram.org/bots/api/#transactionpartneruser)
* [TransactionPartnerChat](https://core.telegram.org/bots/api/#transactionpartnerchat)
* [TransactionPartnerAffiliateProgram](https://core.telegram.org/bots/api/#transactionpartneraffiliateprogram)
* [TransactionPartnerFragment](https://core.telegram.org/bots/api/#transactionpartnerfragment)
* [TransactionPartnerTelegramAds](https://core.telegram.org/bots/api/#transactionpartnertelegramads)
* [TransactionPartnerTelegramApi](https://core.telegram.org/bots/api/#transactionpartnertelegramapi)
* [TransactionPartnerOther](https://core.telegram.org/bots/api/#transactionpartnerother)"""


class TransactionPartnerUser(BaseModel):
    """Describes a transaction with a user.

    https://core.telegram.org/bots/api/#transactionpartneruser
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "user"
    """type_ (str): Type of the transaction partner, always “user”"""
    user: "User"
    """user ("User"): Information about the user"""
    affiliate: Optional["AffiliateInfo"] = None
    """affiliate ("AffiliateInfo"): *Optional*. Information about the affiliate that received a commission via this transaction"""
    invoice_payload: Optional[str] = None
    """invoice_payload (str): *Optional*. Bot-specified invoice payload"""
    subscription_period: Optional[int] = None
    """subscription_period (int): *Optional*. The duration of the paid subscription"""
    paid_media: Optional[List["PaidMedia"]] = None
    """paid_media (List["PaidMedia"]): *Optional*. Information about the paid media bought by the user"""
    paid_media_payload: Optional[str] = None
    """paid_media_payload (str): *Optional*. Bot-specified paid media payload"""
    gift: Optional["Gift"] = None
    """gift ("Gift"): *Optional*. The gift sent to the user by the bot"""


class TransactionPartnerChat(BaseModel):
    """Describes a transaction with a chat.

    https://core.telegram.org/bots/api/#transactionpartnerchat
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "chat"
    """type_ (str): Type of the transaction partner, always “chat”"""
    chat: "Chat"
    """chat ("Chat"): Information about the chat"""
    gift: Optional["Gift"] = None
    """gift ("Gift"): *Optional*. The gift sent to the chat by the bot"""


class TransactionPartnerAffiliateProgram(BaseModel):
    """Describes the affiliate program that issued the affiliate commission received via this transaction.

    https://core.telegram.org/bots/api/#transactionpartneraffiliateprogram
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "affiliate_program"
    """type_ (str): Type of the transaction partner, always “affiliate_program”"""
    sponsor_user: Optional["User"] = None
    """sponsor_user ("User"): *Optional*. Information about the bot that sponsored the affiliate program"""
    commission_per_mille: int
    """commission_per_mille (int): The number of Telegram Stars received by the bot for each 1000 Telegram Stars received by the affiliate program sponsor from referred users"""


class TransactionPartnerFragment(BaseModel):
    """Describes a withdrawal transaction with Fragment.

    https://core.telegram.org/bots/api/#transactionpartnerfragment
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "fragment"
    """type_ (str): Type of the transaction partner, always “fragment”"""
    withdrawal_state: Optional["RevenueWithdrawalState"] = None
    """withdrawal_state ("RevenueWithdrawalState"): *Optional*. State of the transaction if the transaction is outgoing"""


class TransactionPartnerTelegramAds(BaseModel):
    """Describes a withdrawal transaction to the Telegram Ads platform.

    https://core.telegram.org/bots/api/#transactionpartnertelegramads
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "telegram_ads"
    """type_ (str): Type of the transaction partner, always “telegram_ads”"""


class TransactionPartnerTelegramApi(BaseModel):
    """Describes a transaction with payment for [paid broadcasting](https://core.telegram.org/bots/api/#paid-broadcasts).

    https://core.telegram.org/bots/api/#transactionpartnertelegramapi
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "telegram_api"
    """type_ (str): Type of the transaction partner, always “telegram_api”"""
    request_count: int
    """request_count (int): The number of successful requests that exceeded regular limits and were therefore billed"""


class TransactionPartnerOther(BaseModel):
    """Describes a transaction with an unknown source or recipient.

    https://core.telegram.org/bots/api/#transactionpartnerother
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str = "other"
    """type_ (str): Type of the transaction partner, always “other”"""


class StarTransaction(BaseModel):
    """Describes a Telegram Star transaction. Note that if the buyer initiates a chargeback with the payment provider from whom they acquired Stars (e.g., Apple, Google) following this transaction, the refunded Stars will be deducted from the bot's balance. This is outside of Telegram's control.

    https://core.telegram.org/bots/api/#startransaction
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    id: str
    """id (str): Unique identifier of the transaction. Coincides with the identifier of the original transaction for refund transactions. Coincides with *SuccessfulPayment.telegram_payment_charge_id* for successful incoming payments from users."""
    amount: int
    """amount (int): Integer amount of Telegram Stars transferred by the transaction"""
    nanostar_amount: Optional[int] = None
    """nanostar_amount (int): *Optional*. The number of 1/1000000000 shares of Telegram Stars transferred by the transaction; from 0 to 999999999"""
    date: int
    """date (int): Date the transaction was created in Unix time"""
    source: Optional["TransactionPartner"] = None
    """source ("TransactionPartner"): *Optional*. Source of an incoming transaction (e.g., a user purchasing goods or services, Fragment refunding a failed withdrawal). Only for incoming transactions"""
    receiver: Optional["TransactionPartner"] = None
    """receiver ("TransactionPartner"): *Optional*. Receiver of an outgoing transaction (e.g., a user for a purchase refund, Fragment for a withdrawal). Only for outgoing transactions"""


class StarTransactions(BaseModel):
    """Contains a list of Telegram Star transactions.

    https://core.telegram.org/bots/api/#startransactions
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    transactions: List["StarTransaction"]
    """transactions (List["StarTransaction"]): The list of transactions"""


class PassportData(BaseModel):
    """Describes Telegram Passport data shared with the bot by the user.

    https://core.telegram.org/bots/api/#passportdata
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    data: List["EncryptedPassportElement"]
    """data (List["EncryptedPassportElement"]): Array with information about documents and other Telegram Passport elements that was shared with the bot"""
    credentials: "EncryptedCredentials"
    """credentials ("EncryptedCredentials"): Encrypted credentials required to decrypt the data"""


class PassportFile(BaseModel):
    """This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB.

    https://core.telegram.org/bots/api/#passportfile
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    file_id: str
    """file_id (str): Identifier for this file, which can be used to download or reuse the file"""
    file_unique_id: str
    """file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file."""
    file_size: int
    """file_size (int): File size in bytes"""
    file_date: int
    """file_date (int): Unix time when the file was uploaded"""


class EncryptedPassportElement(BaseModel):
    """Describes documents or other Telegram Passport elements shared with the bot by the user.

    https://core.telegram.org/bots/api/#encryptedpassportelement
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    type_: str
    """type_ (str): Element type. One of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”, “phone_number”, “email”."""
    data: Optional[str] = None
    """data (str): *Optional*. Base64-encoded encrypted Telegram Passport element data provided by the user; available only for “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport” and “address” types. Can be decrypted and verified using the accompanying [EncryptedCredentials](https://core.telegram.org/bots/api/#encryptedcredentials)."""
    phone_number: Optional[str] = None
    """phone_number (str): *Optional*. User's verified phone number; available only for “phone_number” type"""
    email: Optional[str] = None
    """email (str): *Optional*. User's verified email address; available only for “email” type"""
    files: Optional[List["PassportFile"]] = None
    """files (List["PassportFile"]): *Optional*. Array of encrypted files with documents provided by the user; available only for “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying [EncryptedCredentials](https://core.telegram.org/bots/api/#encryptedcredentials)."""
    front_side: Optional["PassportFile"] = None
    """front_side ("PassportFile"): *Optional*. Encrypted file with the front side of the document, provided by the user; available only for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying [EncryptedCredentials](https://core.telegram.org/bots/api/#encryptedcredentials)."""
    reverse_side: Optional["PassportFile"] = None
    """reverse_side ("PassportFile"): *Optional*. Encrypted file with the reverse side of the document, provided by the user; available only for “driver_license” and “identity_card”. The file can be decrypted and verified using the accompanying [EncryptedCredentials](https://core.telegram.org/bots/api/#encryptedcredentials)."""
    selfie: Optional["PassportFile"] = None
    """selfie ("PassportFile"): *Optional*. Encrypted file with the selfie of the user holding a document, provided by the user; available if requested for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying [EncryptedCredentials](https://core.telegram.org/bots/api/#encryptedcredentials)."""
    translation: Optional[List["PassportFile"]] = None
    """translation (List["PassportFile"]): *Optional*. Array of encrypted files with translated versions of documents provided by the user; available if requested for “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying [EncryptedCredentials](https://core.telegram.org/bots/api/#encryptedcredentials)."""
    hash: str
    """hash (str): Base64-encoded element hash for using in [PassportElementErrorUnspecified](https://core.telegram.org/bots/api/#passportelementerrorunspecified)"""


class EncryptedCredentials(BaseModel):
    """Describes data required for decrypting and authenticating [EncryptedPassportElement](https://core.telegram.org/bots/api/#encryptedpassportelement). See the [Telegram Passport Documentation](https://core.telegram.org/passport#receiving-information) for a complete description of the data decryption and authentication processes.

    https://core.telegram.org/bots/api/#encryptedcredentials
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    data: str
    """data (str): Base64-encoded encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for [EncryptedPassportElement](https://core.telegram.org/bots/api/#encryptedpassportelement) decryption and authentication"""
    hash: str
    """hash (str): Base64-encoded data hash for data authentication"""
    secret: str
    """secret (str): Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption"""


PassportElementError = Union["PassportElementErrorDataField", "PassportElementErrorFrontSide", "PassportElementErrorReverseSide", "PassportElementErrorSelfie",
                             "PassportElementErrorFile", "PassportElementErrorFiles", "PassportElementErrorTranslationFile", "PassportElementErrorTranslationFiles", "PassportElementErrorUnspecified"]
"""This object represents an error in the Telegram Passport element which was submitted that should be resolved by the user. It should be one of:

* [PassportElementErrorDataField](https://core.telegram.org/bots/api/#passportelementerrordatafield)
* [PassportElementErrorFrontSide](https://core.telegram.org/bots/api/#passportelementerrorfrontside)
* [PassportElementErrorReverseSide](https://core.telegram.org/bots/api/#passportelementerrorreverseside)
* [PassportElementErrorSelfie](https://core.telegram.org/bots/api/#passportelementerrorselfie)
* [PassportElementErrorFile](https://core.telegram.org/bots/api/#passportelementerrorfile)
* [PassportElementErrorFiles](https://core.telegram.org/bots/api/#passportelementerrorfiles)
* [PassportElementErrorTranslationFile](https://core.telegram.org/bots/api/#passportelementerrortranslationfile)
* [PassportElementErrorTranslationFiles](https://core.telegram.org/bots/api/#passportelementerrortranslationfiles)
* [PassportElementErrorUnspecified](https://core.telegram.org/bots/api/#passportelementerrorunspecified)"""


class PassportElementErrorDataField(BaseModel):
    """Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.

    https://core.telegram.org/bots/api/#passportelementerrordatafield
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    source: str = "data"
    """source (str): Error source, must be *data*"""
    type_: str
    """type_ (str): The section of the user's Telegram Passport which has the error, one of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”"""
    field_name: str
    """field_name (str): Name of the data field which has the error"""
    data_hash: str
    """data_hash (str): Base64-encoded data hash"""
    message: str
    """message (str): Error message"""


class PassportElementErrorFrontSide(BaseModel):
    """Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes.

    https://core.telegram.org/bots/api/#passportelementerrorfrontside
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    source: str = "front_side"
    """source (str): Error source, must be *front_side*"""
    type_: str
    """type_ (str): The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”"""
    file_hash: str
    """file_hash (str): Base64-encoded hash of the file with the front side of the document"""
    message: str
    """message (str): Error message"""


class PassportElementErrorReverseSide(BaseModel):
    """Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes.

    https://core.telegram.org/bots/api/#passportelementerrorreverseside
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    source: str = "reverse_side"
    """source (str): Error source, must be *reverse_side*"""
    type_: str
    """type_ (str): The section of the user's Telegram Passport which has the issue, one of “driver_license”, “identity_card”"""
    file_hash: str
    """file_hash (str): Base64-encoded hash of the file with the reverse side of the document"""
    message: str
    """message (str): Error message"""


class PassportElementErrorSelfie(BaseModel):
    """Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.

    https://core.telegram.org/bots/api/#passportelementerrorselfie
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    source: str = "selfie"
    """source (str): Error source, must be *selfie*"""
    type_: str
    """type_ (str): The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”"""
    file_hash: str
    """file_hash (str): Base64-encoded hash of the file with the selfie"""
    message: str
    """message (str): Error message"""


class PassportElementErrorFile(BaseModel):
    """Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.

    https://core.telegram.org/bots/api/#passportelementerrorfile
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    source: str = "file"
    """source (str): Error source, must be *file*"""
    type_: str
    """type_ (str): The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”"""
    file_hash: str
    """file_hash (str): Base64-encoded file hash"""
    message: str
    """message (str): Error message"""


class PassportElementErrorFiles(BaseModel):
    """Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.

    https://core.telegram.org/bots/api/#passportelementerrorfiles
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    source: str = "files"
    """source (str): Error source, must be *files*"""
    type_: str
    """type_ (str): The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”"""
    file_hashes: List[str]
    """file_hashes (List[str]): List of base64-encoded file hashes"""
    message: str
    """message (str): Error message"""


class PassportElementErrorTranslationFile(BaseModel):
    """Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.

    https://core.telegram.org/bots/api/#passportelementerrortranslationfile
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    source: str = "translation_file"
    """source (str): Error source, must be *translation_file*"""
    type_: str
    """type_ (str): Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”"""
    file_hash: str
    """file_hash (str): Base64-encoded file hash"""
    message: str
    """message (str): Error message"""


class PassportElementErrorTranslationFiles(BaseModel):
    """Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.

    https://core.telegram.org/bots/api/#passportelementerrortranslationfiles
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    source: str = "translation_files"
    """source (str): Error source, must be *translation_files*"""
    type_: str
    """type_ (str): Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”"""
    file_hashes: List[str]
    """file_hashes (List[str]): List of base64-encoded file hashes"""
    message: str
    """message (str): Error message"""


class PassportElementErrorUnspecified(BaseModel):
    """Represents an issue in an unspecified place. The error is considered resolved when new data is added.

    https://core.telegram.org/bots/api/#passportelementerrorunspecified
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    source: str = "unspecified"
    """source (str): Error source, must be *unspecified*"""
    type_: str
    """type_ (str): Type of element of the user's Telegram Passport which has the issue"""
    element_hash: str
    """element_hash (str): Base64-encoded element hash"""
    message: str
    """message (str): Error message"""


class Game(BaseModel):
    """This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.

    https://core.telegram.org/bots/api/#game
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    title: str
    """title (str): Title of the game"""
    description: str
    """description (str): Description of the game"""
    photo: List["PhotoSize"]
    """photo (List["PhotoSize"]): Photo that will be displayed in the game message in chats."""
    text: Optional[str] = None
    """text (str): *Optional*. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls [setGameScore](https://core.telegram.org/bots/api/#setgamescore), or manually edited using [editMessageText](https://core.telegram.org/bots/api/#editmessagetext). 0-4096 characters."""
    text_entities: Optional[List["MessageEntity"]] = None
    """text_entities (List["MessageEntity"]): *Optional*. Special entities that appear in *text*, such as usernames, URLs, bot commands, etc."""
    animation: Optional["Animation"] = None
    """animation ("Animation"): *Optional*. Animation that will be displayed in the game message in chats. Upload via [BotFather](https://t.me/botfather)"""


CallbackGame = Any
"""A placeholder, currently holds no information. Use [BotFather](https://t.me/botfather) to set up your game."""


class GameHighScore(BaseModel):
    """This object represents one row of the high scores table for a game.

    https://core.telegram.org/bots/api/#gamehighscore
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    position: int
    """position (int): Position in high score table for the game"""
    user: "User"
    """user ("User"): User"""
    score: int
    """score (int): Score"""
