
from typing import Dict, Union, Optional, List, TypeVar, Generic, Type

from httpx import AsyncClient    
from pydantic import BaseModel
            
from alya_types import objects
            

# pylint: disable=C0301,C0302
T = TypeVar('T')
            

class ApiResponse(BaseModel, Generic[T]):
    ok: bool
    result: T

class ApiWrapper:
    def __init__(self, token: str, *, api_url: str = "https://api.telegram.org/"):
        self.token = token
        self.api_url = api_url
        self.client = AsyncClient(
            base_url=api_url + "bot" + token + '/'
        )

    async def exec_request(
            self,
            method: str,
            json: Dict,
            return_type: Type[T]
    ) -> T:
        result = await self.client.post(
            method,
            json=json
        )
        mdl = ApiResponse[return_type]  # type: ignore
        response = mdl.model_validate(result.json())
        return response.result

    async def get_updates(self, *, offset: Optional[int] = None, limit: Optional[int] = 100, timeout: Optional[int] = None, allowed_updates: Optional[List[str]] = None) -> List[objects.Update]:
        """Use this method to receive incoming updates using long polling ([wiki](https://en.wikipedia.org/wiki/Push_technology#Long_polling)). Returns an Array of [Update](https://core.telegram.org/bots/api/#update) objects.

        Args:
            offset (int): Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as [getUpdates](https://core.telegram.org/bots/api/#getupdates) is called with an *offset* higher than its *update_id*. The negative offset can be specified to retrieve updates starting from *-offset* update from the end of the updates queue. All previous updates will be forgotten.
            limit (int): Limits the number of updates to be retrieved. Values between 1-100 are accepted. Defaults to 100.
            timeout (int): Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling. Should be positive, short polling should be used for testing purposes only.
            allowed_updates (List[str]): A JSON-serialized list of the update types you want your bot to receive. For example, specify `['message', 'edited_channel_post', 'callback_query']` to only receive updates of these types. See [Update](https://core.telegram.org/bots/api/#update) for a complete list of available update types. Specify an empty list to receive all update types except *chat_member*, *message_reaction*, and *message_reaction_count* (default). If not specified, the previous setting will be used.  

Please note that this parameter doesn't affect updates created before the call to getUpdates, so unwanted updates may be received for a short period of time.
        """
        response_api: List[objects.Update] = await self.exec_request(
            "getUpdates",
            json={"offset": offset,
                  "limit": limit,
                  "timeout": timeout,
                  "allowed_updates": allowed_updates},
            return_type=List[objects.Update]  # type: ignore

        )
        return response_api

    async def set_webhook(self, url: str, *, certificate: Optional[objects.InputFile] = None, ip_address: Optional[str] = None, max_connections: Optional[int] = 40, allowed_updates: Optional[List[str]] = None, drop_pending_updates: Optional[bool] = None, secret_token: Optional[str] = None) -> bool:
        """Use this method to specify a URL and receive incoming updates via an outgoing webhook. Whenever there is an update for the bot, we will send an HTTPS POST request to the specified URL, containing a JSON-serialized [Update](https://core.telegram.org/bots/api/#update). In case of an unsuccessful request (a request with response [HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) different from `2XY`), we will repeat the request and give up after a reasonable amount of attempts. Returns *True* on success.

If you'd like to make sure that the webhook was set by you, you can specify secret data in the parameter *secret_token*. If specified, the request will contain a header “X-Telegram-Bot-Api-Secret-Token” with the secret token as content.

        Args:
            url (str): HTTPS URL to send updates to. Use an empty string to remove webhook integration
            certificate ("InputFile"): Upload your public key certificate so that the root certificate in use can be checked. See our [self-signed guide](https://core.telegram.org/bots/self-signed) for details.
            ip_address (str): The fixed IP address which will be used to send webhook requests instead of the IP address resolved through DNS
            max_connections (int): The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery, 1-100. Defaults to *40*. Use lower values to limit the load on your bot's server, and higher values to increase your bot's throughput.
            allowed_updates (List[str]): A JSON-serialized list of the update types you want your bot to receive. For example, specify `['message', 'edited_channel_post', 'callback_query']` to only receive updates of these types. See [Update](https://core.telegram.org/bots/api/#update) for a complete list of available update types. Specify an empty list to receive all update types except *chat_member*, *message_reaction*, and *message_reaction_count* (default). If not specified, the previous setting will be used.  
Please note that this parameter doesn't affect updates created before the call to the setWebhook, so unwanted updates may be received for a short period of time.
            drop_pending_updates (bool): Pass *True* to drop all pending updates
            secret_token (str): A secret token to be sent in a header “X-Telegram-Bot-Api-Secret-Token” in every webhook request, 1-256 characters. Only characters `A-Z`, `a-z`, `0-9`, `_` and `-` are allowed. The header is useful to ensure that the request comes from a webhook set by you.
        """
        response_api: bool = await self.exec_request(
            "setWebhook",
            json={"url": url,
                  "certificate": certificate,
                  "ip_address": ip_address,
                  "max_connections": max_connections,
                  "allowed_updates": allowed_updates,
                  "drop_pending_updates": drop_pending_updates,
                  "secret_token": secret_token},
            return_type=bool  # type: ignore

        )
        return response_api

    async def delete_webhook(self, *, drop_pending_updates: Optional[bool] = None) -> bool:
        """Use this method to remove webhook integration if you decide to switch back to [getUpdates](https://core.telegram.org/bots/api/#getupdates). Returns *True* on success.

        Args:
            drop_pending_updates (bool): Pass *True* to drop all pending updates
        """
        response_api: bool = await self.exec_request(
            "deleteWebhook",
            json={"drop_pending_updates": drop_pending_updates},
            return_type=bool  # type: ignore

        )
        return response_api

    async def get_webhook_info(self) -> objects.WebhookInfo:
        """Use this method to get current webhook status. Requires no parameters. On success, returns a [WebhookInfo](https://core.telegram.org/bots/api/#webhookinfo) object. If the bot is using [getUpdates](https://core.telegram.org/bots/api/#getupdates), will return an object with the *url* field empty.

        Args:

        """
        response_api: objects.WebhookInfo = await self.exec_request(
            "getWebhookInfo",
            json={},
            return_type=objects.WebhookInfo  # type: ignore

        )
        return response_api

    async def get_me(self) -> objects.User:
        """A simple method for testing your bot's authentication token. Requires no parameters. Returns basic information about the bot in form of a [User](https://core.telegram.org/bots/api/#user) object.

        Args:

        """
        response_api: objects.User = await self.exec_request(
            "getMe",
            json={},
            return_type=objects.User  # type: ignore

        )
        return response_api

    async def log_out(self) -> bool:
        """Use this method to log out from the cloud Bot API server before launching the bot locally. You **must** log out the bot before running it locally, otherwise there is no guarantee that the bot will receive updates. After a successful call, you can immediately log in on a local server, but will not be able to log in back to the cloud Bot API server for 10 minutes. Returns *True* on success. Requires no parameters.

        Args:

        """
        response_api: bool = await self.exec_request(
            "logOut",
            json={},
            return_type=bool  # type: ignore

        )
        return response_api

    async def close(self) -> bool:
        """Use this method to close the bot instance before moving it from one local server to another. You need to delete the webhook before calling this method to ensure that the bot isn't launched again after server restart. The method will return error 429 in the first 10 minutes after the bot is launched. Returns *True* on success. Requires no parameters.

        Args:

        """
        response_api: bool = await self.exec_request(
            "close",
            json={},
            return_type=bool  # type: ignore

        )
        return response_api

    async def send_message(self, chat_id: Union[int, str], text: str, *, business_connection_id: Optional[str] = None, message_thread_id: Optional[int] = None, parse_mode: Optional[str] = None, entities: Optional[List[objects.MessageEntity]] = None, link_preview_options: Optional[objects.LinkPreviewOptions] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None, allow_paid_broadcast: Optional[bool] = None, message_effect_id: Optional[str] = None, reply_parameters: Optional[objects.ReplyParameters] = None, reply_markup: Optional[Union[objects.InlineKeyboardMarkup, objects.ReplyKeyboardMarkup, objects.ReplyKeyboardRemove, objects.ForceReply]] = None) -> objects.Message:
        """Use this method to send text messages. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message will be sent
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
            text (str): Text of the message to be sent, 1-4096 characters after entities parsing
            parse_mode (str): Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
            entities (List["MessageEntity"]): A JSON-serialized list of special entities that appear in message text, which can be specified instead of *parse_mode*
            link_preview_options ("LinkPreviewOptions"): Link preview generation options for the message
            disable_notification (bool): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
            protect_content (bool): Protects the contents of the sent message from forwarding and saving
            allow_paid_broadcast (bool): Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance
            message_effect_id (str): Unique identifier of the message effect to be added to the message; for private chats only
            reply_parameters ("ReplyParameters"): Description of the message to reply to
            reply_markup (Union["InlineKeyboardMarkup", "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]): Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
        """
        response_api: objects.Message = await self.exec_request(
            "sendMessage",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "text": text,
                  "parse_mode": parse_mode,
                  "entities": entities,
                  "link_preview_options": link_preview_options,
                  "disable_notification": disable_notification,
                  "protect_content": protect_content,
                  "allow_paid_broadcast": allow_paid_broadcast,
                  "message_effect_id": message_effect_id,
                  "reply_parameters": reply_parameters,
                  "reply_markup": reply_markup},
            return_type=objects.Message  # type: ignore

        )
        return response_api

    async def forward_message(self, chat_id: Union[int, str], from_chat_id: Union[int, str], message_id: int, *, message_thread_id: Optional[int] = None, video_start_timestamp: Optional[int] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None) -> objects.Message:
        """Use this method to forward messages of any kind. Service messages and messages with protected content can't be forwarded. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
            from_chat_id (Union[int, str]): Unique identifier for the chat where the original message was sent (or channel username in the format `@channelusername`)
            video_start_timestamp (int): New start timestamp for the forwarded video in the message
            disable_notification (bool): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
            protect_content (bool): Protects the contents of the forwarded message from forwarding and saving
            message_id (int): Message identifier in the chat specified in *from_chat_id*
        """
        response_api: objects.Message = await self.exec_request(
            "forwardMessage",
            json={"chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "from_chat_id": from_chat_id,
                  "video_start_timestamp": video_start_timestamp,
                  "disable_notification": disable_notification,
                  "protect_content": protect_content,
                  "message_id": message_id},
            return_type=objects.Message  # type: ignore

        )
        return response_api

    async def forward_messages(self, chat_id: Union[int, str], from_chat_id: Union[int, str], message_ids: List[int], *, message_thread_id: Optional[int] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None) -> List[objects.MessageId]:
        """Use this method to forward multiple messages of any kind. If some of the specified messages can't be found or forwarded, they are skipped. Service messages and messages with protected content can't be forwarded. Album grouping is kept for forwarded messages. On success, an array of [MessageId](https://core.telegram.org/bots/api/#messageid) of the sent messages is returned.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
            from_chat_id (Union[int, str]): Unique identifier for the chat where the original messages were sent (or channel username in the format `@channelusername`)
            message_ids (List[int]): A JSON-serialized list of 1-100 identifiers of messages in the chat *from_chat_id* to forward. The identifiers must be specified in a strictly increasing order.
            disable_notification (bool): Sends the messages [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
            protect_content (bool): Protects the contents of the forwarded messages from forwarding and saving
        """
        response_api: List[objects.MessageId] = await self.exec_request(
            "forwardMessages",
            json={"chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "from_chat_id": from_chat_id,
                  "message_ids": message_ids,
                  "disable_notification": disable_notification,
                  "protect_content": protect_content},
            return_type=List[objects.MessageId]  # type: ignore

        )
        return response_api

    async def copy_message(self, chat_id: Union[int, str], from_chat_id: Union[int, str], message_id: int, *, message_thread_id: Optional[int] = None, video_start_timestamp: Optional[int] = None, caption: Optional[str] = None, parse_mode: Optional[str] = None, caption_entities: Optional[List[objects.MessageEntity]] = None, show_caption_above_media: Optional[bool] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None, allow_paid_broadcast: Optional[bool] = None, reply_parameters: Optional[objects.ReplyParameters] = None, reply_markup: Optional[Union[objects.InlineKeyboardMarkup, objects.ReplyKeyboardMarkup, objects.ReplyKeyboardRemove, objects.ForceReply]] = None) -> objects.MessageId:
        """Use this method to copy messages of any kind. Service messages, paid media messages, giveaway messages, giveaway winners messages, and invoice messages can't be copied. A quiz [poll](https://core.telegram.org/bots/api/#poll) can be copied only if the value of the field *correct_option_id* is known to the bot. The method is analogous to the method [forwardMessage](https://core.telegram.org/bots/api/#forwardmessage), but the copied message doesn't have a link to the original message. Returns the [MessageId](https://core.telegram.org/bots/api/#messageid) of the sent message on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
            from_chat_id (Union[int, str]): Unique identifier for the chat where the original message was sent (or channel username in the format `@channelusername`)
            message_id (int): Message identifier in the chat specified in *from_chat_id*
            video_start_timestamp (int): New start timestamp for the copied video in the message
            caption (str): New caption for media, 0-1024 characters after entities parsing. If not specified, the original caption is kept
            parse_mode (str): Mode for parsing entities in the new caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
            caption_entities (List["MessageEntity"]): A JSON-serialized list of special entities that appear in the new caption, which can be specified instead of *parse_mode*
            show_caption_above_media (bool): Pass *True*, if the caption must be shown above the message media. Ignored if a new caption isn't specified.
            disable_notification (bool): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
            protect_content (bool): Protects the contents of the sent message from forwarding and saving
            allow_paid_broadcast (bool): Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance
            reply_parameters ("ReplyParameters"): Description of the message to reply to
            reply_markup (Union["InlineKeyboardMarkup", "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]): Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
        """
        response_api: objects.MessageId = await self.exec_request(
            "copyMessage",
            json={"chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "from_chat_id": from_chat_id,
                  "message_id": message_id,
                  "video_start_timestamp": video_start_timestamp,
                  "caption": caption,
                  "parse_mode": parse_mode,
                  "caption_entities": caption_entities,
                  "show_caption_above_media": show_caption_above_media,
                  "disable_notification": disable_notification,
                  "protect_content": protect_content,
                  "allow_paid_broadcast": allow_paid_broadcast,
                  "reply_parameters": reply_parameters,
                  "reply_markup": reply_markup},
            return_type=objects.MessageId  # type: ignore

        )
        return response_api

    async def copy_messages(self, chat_id: Union[int, str], from_chat_id: Union[int, str], message_ids: List[int], *, message_thread_id: Optional[int] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None, remove_caption: Optional[bool] = None) -> List[objects.MessageId]:
        """Use this method to copy messages of any kind. If some of the specified messages can't be found or copied, they are skipped. Service messages, paid media messages, giveaway messages, giveaway winners messages, and invoice messages can't be copied. A quiz [poll](https://core.telegram.org/bots/api/#poll) can be copied only if the value of the field *correct_option_id* is known to the bot. The method is analogous to the method [forwardMessages](https://core.telegram.org/bots/api/#forwardmessages), but the copied messages don't have a link to the original message. Album grouping is kept for copied messages. On success, an array of [MessageId](https://core.telegram.org/bots/api/#messageid) of the sent messages is returned.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
            from_chat_id (Union[int, str]): Unique identifier for the chat where the original messages were sent (or channel username in the format `@channelusername`)
            message_ids (List[int]): A JSON-serialized list of 1-100 identifiers of messages in the chat *from_chat_id* to copy. The identifiers must be specified in a strictly increasing order.
            disable_notification (bool): Sends the messages [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
            protect_content (bool): Protects the contents of the sent messages from forwarding and saving
            remove_caption (bool): Pass *True* to copy the messages without their captions
        """
        response_api: List[objects.MessageId] = await self.exec_request(
            "copyMessages",
            json={"chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "from_chat_id": from_chat_id,
                  "message_ids": message_ids,
                  "disable_notification": disable_notification,
                  "protect_content": protect_content,
                  "remove_caption": remove_caption},
            return_type=List[objects.MessageId]  # type: ignore

        )
        return response_api

    async def send_photo(self, chat_id: Union[int, str], photo: Union[objects.InputFile, str], *, business_connection_id: Optional[str] = None, message_thread_id: Optional[int] = None, caption: Optional[str] = None, parse_mode: Optional[str] = None, caption_entities: Optional[List[objects.MessageEntity]] = None, show_caption_above_media: Optional[bool] = None, has_spoiler: Optional[bool] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None, allow_paid_broadcast: Optional[bool] = None, message_effect_id: Optional[str] = None, reply_parameters: Optional[objects.ReplyParameters] = None, reply_markup: Optional[Union[objects.InlineKeyboardMarkup, objects.ReplyKeyboardMarkup, objects.ReplyKeyboardRemove, objects.ForceReply]] = None) -> objects.Message:
        """Use this method to send photos. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message will be sent
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
            photo (Union["InputFile", str]): Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)
            caption (str): Photo caption (may also be used when resending photos by *file_id*), 0-1024 characters after entities parsing
            parse_mode (str): Mode for parsing entities in the photo caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
            caption_entities (List["MessageEntity"]): A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            show_caption_above_media (bool): Pass *True*, if the caption must be shown above the message media
            has_spoiler (bool): Pass *True* if the photo needs to be covered with a spoiler animation
            disable_notification (bool): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
            protect_content (bool): Protects the contents of the sent message from forwarding and saving
            allow_paid_broadcast (bool): Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance
            message_effect_id (str): Unique identifier of the message effect to be added to the message; for private chats only
            reply_parameters ("ReplyParameters"): Description of the message to reply to
            reply_markup (Union["InlineKeyboardMarkup", "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]): Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
        """
        response_api: objects.Message = await self.exec_request(
            "sendPhoto",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "photo": photo,
                  "caption": caption,
                  "parse_mode": parse_mode,
                  "caption_entities": caption_entities,
                  "show_caption_above_media": show_caption_above_media,
                  "has_spoiler": has_spoiler,
                  "disable_notification": disable_notification,
                  "protect_content": protect_content,
                  "allow_paid_broadcast": allow_paid_broadcast,
                  "message_effect_id": message_effect_id,
                  "reply_parameters": reply_parameters,
                  "reply_markup": reply_markup},
            return_type=objects.Message  # type: ignore

        )
        return response_api

    async def send_audio(self, chat_id: Union[int, str], audio: Union[objects.InputFile, str], *, business_connection_id: Optional[str] = None, message_thread_id: Optional[int] = None, caption: Optional[str] = None, parse_mode: Optional[str] = None, caption_entities: Optional[List[objects.MessageEntity]] = None, duration: Optional[int] = None, performer: Optional[str] = None, title: Optional[str] = None, thumbnail: Optional[Union[objects.InputFile, str]] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None, allow_paid_broadcast: Optional[bool] = None, message_effect_id: Optional[str] = None, reply_parameters: Optional[objects.ReplyParameters] = None, reply_markup: Optional[Union[objects.InlineKeyboardMarkup, objects.ReplyKeyboardMarkup, objects.ReplyKeyboardRemove, objects.ForceReply]] = None) -> objects.Message:
        """Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.

For sending voice messages, use the [sendVoice](https://core.telegram.org/bots/api/#sendvoice) method instead.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message will be sent
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
            audio (Union["InputFile", str]): Audio file to send. Pass a file_id as String to send an audio file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)
            caption (str): Audio caption, 0-1024 characters after entities parsing
            parse_mode (str): Mode for parsing entities in the audio caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
            caption_entities (List["MessageEntity"]): A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            duration (int): Duration of the audio in seconds
            performer (str): Performer
            title (str): Track name
            thumbnail (Union["InputFile", str]): Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)
            disable_notification (bool): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
            protect_content (bool): Protects the contents of the sent message from forwarding and saving
            allow_paid_broadcast (bool): Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance
            message_effect_id (str): Unique identifier of the message effect to be added to the message; for private chats only
            reply_parameters ("ReplyParameters"): Description of the message to reply to
            reply_markup (Union["InlineKeyboardMarkup", "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]): Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
        """
        response_api: objects.Message = await self.exec_request(
            "sendAudio",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "audio": audio,
                  "caption": caption,
                  "parse_mode": parse_mode,
                  "caption_entities": caption_entities,
                  "duration": duration,
                  "performer": performer,
                  "title": title,
                  "thumbnail": thumbnail,
                  "disable_notification": disable_notification,
                  "protect_content": protect_content,
                  "allow_paid_broadcast": allow_paid_broadcast,
                  "message_effect_id": message_effect_id,
                  "reply_parameters": reply_parameters,
                  "reply_markup": reply_markup},
            return_type=objects.Message  # type: ignore

        )
        return response_api

    async def send_document(self, chat_id: Union[int, str], document: Union[objects.InputFile, str], *, business_connection_id: Optional[str] = None, message_thread_id: Optional[int] = None, thumbnail: Optional[Union[objects.InputFile, str]] = None, caption: Optional[str] = None, parse_mode: Optional[str] = None, caption_entities: Optional[List[objects.MessageEntity]] = None, disable_content_type_detection: Optional[bool] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None, allow_paid_broadcast: Optional[bool] = None, message_effect_id: Optional[str] = None, reply_parameters: Optional[objects.ReplyParameters] = None, reply_markup: Optional[Union[objects.InlineKeyboardMarkup, objects.ReplyKeyboardMarkup, objects.ReplyKeyboardRemove, objects.ForceReply]] = None) -> objects.Message:
        """Use this method to send general files. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message will be sent
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
            document (Union["InputFile", str]): File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)
            thumbnail (Union["InputFile", str]): Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)
            caption (str): Document caption (may also be used when resending documents by *file_id*), 0-1024 characters after entities parsing
            parse_mode (str): Mode for parsing entities in the document caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
            caption_entities (List["MessageEntity"]): A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            disable_content_type_detection (bool): Disables automatic server-side content type detection for files uploaded using multipart/form-data
            disable_notification (bool): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
            protect_content (bool): Protects the contents of the sent message from forwarding and saving
            allow_paid_broadcast (bool): Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance
            message_effect_id (str): Unique identifier of the message effect to be added to the message; for private chats only
            reply_parameters ("ReplyParameters"): Description of the message to reply to
            reply_markup (Union["InlineKeyboardMarkup", "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]): Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
        """
        response_api: objects.Message = await self.exec_request(
            "sendDocument",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "document": document,
                  "thumbnail": thumbnail,
                  "caption": caption,
                  "parse_mode": parse_mode,
                  "caption_entities": caption_entities,
                  "disable_content_type_detection": disable_content_type_detection,
                  "disable_notification": disable_notification,
                  "protect_content": protect_content,
                  "allow_paid_broadcast": allow_paid_broadcast,
                  "message_effect_id": message_effect_id,
                  "reply_parameters": reply_parameters,
                  "reply_markup": reply_markup},
            return_type=objects.Message  # type: ignore

        )
        return response_api

    async def send_video(self, chat_id: Union[int, str], video: Union[objects.InputFile, str], *, business_connection_id: Optional[str] = None, message_thread_id: Optional[int] = None, duration: Optional[int] = None, width: Optional[int] = None, height: Optional[int] = None, thumbnail: Optional[Union[objects.InputFile, str]] = None, cover: Optional[Union[objects.InputFile, str]] = None, start_timestamp: Optional[int] = None, caption: Optional[str] = None, parse_mode: Optional[str] = None, caption_entities: Optional[List[objects.MessageEntity]] = None, show_caption_above_media: Optional[bool] = None, has_spoiler: Optional[bool] = None, supports_streaming: Optional[bool] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None, allow_paid_broadcast: Optional[bool] = None, message_effect_id: Optional[str] = None, reply_parameters: Optional[objects.ReplyParameters] = None, reply_markup: Optional[Union[objects.InlineKeyboardMarkup, objects.ReplyKeyboardMarkup, objects.ReplyKeyboardRemove, objects.ForceReply]] = None) -> objects.Message:
        """Use this method to send video files, Telegram clients support MPEG4 videos (other formats may be sent as [Document](https://core.telegram.org/bots/api/#document)). On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message will be sent
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
            video (Union["InputFile", str]): Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)
            duration (int): Duration of sent video in seconds
            width (int): Video width
            height (int): Video height
            thumbnail (Union["InputFile", str]): Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)
            cover (Union["InputFile", str]): Cover for the video in the message. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)
            start_timestamp (int): Start timestamp for the video in the message
            caption (str): Video caption (may also be used when resending videos by *file_id*), 0-1024 characters after entities parsing
            parse_mode (str): Mode for parsing entities in the video caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
            caption_entities (List["MessageEntity"]): A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            show_caption_above_media (bool): Pass *True*, if the caption must be shown above the message media
            has_spoiler (bool): Pass *True* if the video needs to be covered with a spoiler animation
            supports_streaming (bool): Pass *True* if the uploaded video is suitable for streaming
            disable_notification (bool): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
            protect_content (bool): Protects the contents of the sent message from forwarding and saving
            allow_paid_broadcast (bool): Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance
            message_effect_id (str): Unique identifier of the message effect to be added to the message; for private chats only
            reply_parameters ("ReplyParameters"): Description of the message to reply to
            reply_markup (Union["InlineKeyboardMarkup", "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]): Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
        """
        response_api: objects.Message = await self.exec_request(
            "sendVideo",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "video": video,
                  "duration": duration,
                  "width": width,
                  "height": height,
                  "thumbnail": thumbnail,
                  "cover": cover,
                  "start_timestamp": start_timestamp,
                  "caption": caption,
                  "parse_mode": parse_mode,
                  "caption_entities": caption_entities,
                  "show_caption_above_media": show_caption_above_media,
                  "has_spoiler": has_spoiler,
                  "supports_streaming": supports_streaming,
                  "disable_notification": disable_notification,
                  "protect_content": protect_content,
                  "allow_paid_broadcast": allow_paid_broadcast,
                  "message_effect_id": message_effect_id,
                  "reply_parameters": reply_parameters,
                  "reply_markup": reply_markup},
            return_type=objects.Message  # type: ignore

        )
        return response_api

    async def send_animation(self, chat_id: Union[int, str], animation: Union[objects.InputFile, str], *, business_connection_id: Optional[str] = None, message_thread_id: Optional[int] = None, duration: Optional[int] = None, width: Optional[int] = None, height: Optional[int] = None, thumbnail: Optional[Union[objects.InputFile, str]] = None, caption: Optional[str] = None, parse_mode: Optional[str] = None, caption_entities: Optional[List[objects.MessageEntity]] = None, show_caption_above_media: Optional[bool] = None, has_spoiler: Optional[bool] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None, allow_paid_broadcast: Optional[bool] = None, message_effect_id: Optional[str] = None, reply_parameters: Optional[objects.ReplyParameters] = None, reply_markup: Optional[Union[objects.InlineKeyboardMarkup, objects.ReplyKeyboardMarkup, objects.ReplyKeyboardRemove, objects.ForceReply]] = None) -> objects.Message:
        """Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message will be sent
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
            animation (Union["InputFile", str]): Animation to send. Pass a file_id as String to send an animation that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an animation from the Internet, or upload a new animation using multipart/form-data. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)
            duration (int): Duration of sent animation in seconds
            width (int): Animation width
            height (int): Animation height
            thumbnail (Union["InputFile", str]): Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)
            caption (str): Animation caption (may also be used when resending animation by *file_id*), 0-1024 characters after entities parsing
            parse_mode (str): Mode for parsing entities in the animation caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
            caption_entities (List["MessageEntity"]): A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            show_caption_above_media (bool): Pass *True*, if the caption must be shown above the message media
            has_spoiler (bool): Pass *True* if the animation needs to be covered with a spoiler animation
            disable_notification (bool): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
            protect_content (bool): Protects the contents of the sent message from forwarding and saving
            allow_paid_broadcast (bool): Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance
            message_effect_id (str): Unique identifier of the message effect to be added to the message; for private chats only
            reply_parameters ("ReplyParameters"): Description of the message to reply to
            reply_markup (Union["InlineKeyboardMarkup", "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]): Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
        """
        response_api: objects.Message = await self.exec_request(
            "sendAnimation",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "animation": animation,
                  "duration": duration,
                  "width": width,
                  "height": height,
                  "thumbnail": thumbnail,
                  "caption": caption,
                  "parse_mode": parse_mode,
                  "caption_entities": caption_entities,
                  "show_caption_above_media": show_caption_above_media,
                  "has_spoiler": has_spoiler,
                  "disable_notification": disable_notification,
                  "protect_content": protect_content,
                  "allow_paid_broadcast": allow_paid_broadcast,
                  "message_effect_id": message_effect_id,
                  "reply_parameters": reply_parameters,
                  "reply_markup": reply_markup},
            return_type=objects.Message  # type: ignore

        )
        return response_api

    async def send_voice(self, chat_id: Union[int, str], voice: Union[objects.InputFile, str], *, business_connection_id: Optional[str] = None, message_thread_id: Optional[int] = None, caption: Optional[str] = None, parse_mode: Optional[str] = None, caption_entities: Optional[List[objects.MessageEntity]] = None, duration: Optional[int] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None, allow_paid_broadcast: Optional[bool] = None, message_effect_id: Optional[str] = None, reply_parameters: Optional[objects.ReplyParameters] = None, reply_markup: Optional[Union[objects.InlineKeyboardMarkup, objects.ReplyKeyboardMarkup, objects.ReplyKeyboardRemove, objects.ForceReply]] = None) -> objects.Message:
        """Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS, or in .MP3 format, or in .M4A format (other formats may be sent as [Audio](https://core.telegram.org/bots/api/#audio) or [Document](https://core.telegram.org/bots/api/#document)). On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message will be sent
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
            voice (Union["InputFile", str]): Audio file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)
            caption (str): Voice message caption, 0-1024 characters after entities parsing
            parse_mode (str): Mode for parsing entities in the voice message caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
            caption_entities (List["MessageEntity"]): A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            duration (int): Duration of the voice message in seconds
            disable_notification (bool): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
            protect_content (bool): Protects the contents of the sent message from forwarding and saving
            allow_paid_broadcast (bool): Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance
            message_effect_id (str): Unique identifier of the message effect to be added to the message; for private chats only
            reply_parameters ("ReplyParameters"): Description of the message to reply to
            reply_markup (Union["InlineKeyboardMarkup", "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]): Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
        """
        response_api: objects.Message = await self.exec_request(
            "sendVoice",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "voice": voice,
                  "caption": caption,
                  "parse_mode": parse_mode,
                  "caption_entities": caption_entities,
                  "duration": duration,
                  "disable_notification": disable_notification,
                  "protect_content": protect_content,
                  "allow_paid_broadcast": allow_paid_broadcast,
                  "message_effect_id": message_effect_id,
                  "reply_parameters": reply_parameters,
                  "reply_markup": reply_markup},
            return_type=objects.Message  # type: ignore

        )
        return response_api

    async def send_video_note(self, chat_id: Union[int, str], video_note: Union[objects.InputFile, str], *, business_connection_id: Optional[str] = None, message_thread_id: Optional[int] = None, duration: Optional[int] = None, length: Optional[int] = None, thumbnail: Optional[Union[objects.InputFile, str]] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None, allow_paid_broadcast: Optional[bool] = None, message_effect_id: Optional[str] = None, reply_parameters: Optional[objects.ReplyParameters] = None, reply_markup: Optional[Union[objects.InlineKeyboardMarkup, objects.ReplyKeyboardMarkup, objects.ReplyKeyboardRemove, objects.ForceReply]] = None) -> objects.Message:
        """As of [v.4.0](https://telegram.org/blog/video-messages-and-telescope), Telegram clients support rounded square MPEG4 videos of up to 1 minute long. Use this method to send video messages. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message will be sent
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
            video_note (Union["InputFile", str]): Video note to send. Pass a file_id as String to send a video note that exists on the Telegram servers (recommended) or upload a new video using multipart/form-data. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files). Sending video notes by a URL is currently unsupported
            duration (int): Duration of sent video in seconds
            length (int): Video width and height, i.e. diameter of the video message
            thumbnail (Union["InputFile", str]): Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)
            disable_notification (bool): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
            protect_content (bool): Protects the contents of the sent message from forwarding and saving
            allow_paid_broadcast (bool): Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance
            message_effect_id (str): Unique identifier of the message effect to be added to the message; for private chats only
            reply_parameters ("ReplyParameters"): Description of the message to reply to
            reply_markup (Union["InlineKeyboardMarkup", "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]): Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
        """
        response_api: objects.Message = await self.exec_request(
            "sendVideoNote",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "video_note": video_note,
                  "duration": duration,
                  "length": length,
                  "thumbnail": thumbnail,
                  "disable_notification": disable_notification,
                  "protect_content": protect_content,
                  "allow_paid_broadcast": allow_paid_broadcast,
                  "message_effect_id": message_effect_id,
                  "reply_parameters": reply_parameters,
                  "reply_markup": reply_markup},
            return_type=objects.Message  # type: ignore

        )
        return response_api

    async def send_paid_media(self, chat_id: Union[int, str], star_count: int, media: List[objects.InputPaidMedia], *, business_connection_id: Optional[str] = None, payload: Optional[str] = None, caption: Optional[str] = None, parse_mode: Optional[str] = None, caption_entities: Optional[List[objects.MessageEntity]] = None, show_caption_above_media: Optional[bool] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None, allow_paid_broadcast: Optional[bool] = None, reply_parameters: Optional[objects.ReplyParameters] = None, reply_markup: Optional[Union[objects.InlineKeyboardMarkup, objects.ReplyKeyboardMarkup, objects.ReplyKeyboardRemove, objects.ForceReply]] = None) -> objects.Message:
        """Use this method to send paid media. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message will be sent
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`). If the chat is a channel, all Telegram Star proceeds from this media will be credited to the chat's balance. Otherwise, they will be credited to the bot's balance.
            star_count (int): The number of Telegram Stars that must be paid to buy access to the media; 1-2500
            media (List["InputPaidMedia"]): A JSON-serialized array describing the media to be sent; up to 10 items
            payload (str): Bot-defined paid media payload, 0-128 bytes. This will not be displayed to the user, use it for your internal processes.
            caption (str): Media caption, 0-1024 characters after entities parsing
            parse_mode (str): Mode for parsing entities in the media caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
            caption_entities (List["MessageEntity"]): A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            show_caption_above_media (bool): Pass *True*, if the caption must be shown above the message media
            disable_notification (bool): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
            protect_content (bool): Protects the contents of the sent message from forwarding and saving
            allow_paid_broadcast (bool): Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance
            reply_parameters ("ReplyParameters"): Description of the message to reply to
            reply_markup (Union["InlineKeyboardMarkup", "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]): Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
        """
        response_api: objects.Message = await self.exec_request(
            "sendPaidMedia",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "star_count": star_count,
                  "media": media,
                  "payload": payload,
                  "caption": caption,
                  "parse_mode": parse_mode,
                  "caption_entities": caption_entities,
                  "show_caption_above_media": show_caption_above_media,
                  "disable_notification": disable_notification,
                  "protect_content": protect_content,
                  "allow_paid_broadcast": allow_paid_broadcast,
                  "reply_parameters": reply_parameters,
                  "reply_markup": reply_markup},
            return_type=objects.Message  # type: ignore

        )
        return response_api

    async def send_media_group(self, chat_id: Union[int, str], media: List[Union[objects.InputMediaAudio, objects.InputMediaDocument, objects.InputMediaPhoto, objects.InputMediaVideo]], *, business_connection_id: Optional[str] = None, message_thread_id: Optional[int] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None, allow_paid_broadcast: Optional[bool] = None, message_effect_id: Optional[str] = None, reply_parameters: Optional[objects.ReplyParameters] = None) -> List[objects.Message]:
        """Use this method to send a group of photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an array of [Messages](https://core.telegram.org/bots/api/#message) that were sent is returned.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message will be sent
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
            media (List[Union["InputMediaAudio", "InputMediaDocument", "InputMediaPhoto", "InputMediaVideo"]]): A JSON-serialized array describing messages to be sent, must include 2-10 items
            disable_notification (bool): Sends messages [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
            protect_content (bool): Protects the contents of the sent messages from forwarding and saving
            allow_paid_broadcast (bool): Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance
            message_effect_id (str): Unique identifier of the message effect to be added to the message; for private chats only
            reply_parameters ("ReplyParameters"): Description of the message to reply to
        """
        response_api: List[objects.Message] = await self.exec_request(
            "sendMediaGroup",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "media": media,
                  "disable_notification": disable_notification,
                  "protect_content": protect_content,
                  "allow_paid_broadcast": allow_paid_broadcast,
                  "message_effect_id": message_effect_id,
                  "reply_parameters": reply_parameters},
            return_type=List[objects.Message]  # type: ignore

        )
        return response_api

    async def send_location(self, chat_id: Union[int, str], latitude: float, longitude: float, *, business_connection_id: Optional[str] = None, message_thread_id: Optional[int] = None, horizontal_accuracy: Optional[float] = None, live_period: Optional[int] = None, heading: Optional[int] = None, proximity_alert_radius: Optional[int] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None, allow_paid_broadcast: Optional[bool] = None, message_effect_id: Optional[str] = None, reply_parameters: Optional[objects.ReplyParameters] = None, reply_markup: Optional[Union[objects.InlineKeyboardMarkup, objects.ReplyKeyboardMarkup, objects.ReplyKeyboardRemove, objects.ForceReply]] = None) -> objects.Message:
        """Use this method to send point on the map. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message will be sent
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
            latitude (float): Latitude of the location
            longitude (float): Longitude of the location
            horizontal_accuracy (float): The radius of uncertainty for the location, measured in meters; 0-1500
            live_period (int): Period in seconds during which the location will be updated (see [Live Locations](https://telegram.org/blog/live-locations), should be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely.
            heading (int): For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
            proximity_alert_radius (int): For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
            disable_notification (bool): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
            protect_content (bool): Protects the contents of the sent message from forwarding and saving
            allow_paid_broadcast (bool): Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance
            message_effect_id (str): Unique identifier of the message effect to be added to the message; for private chats only
            reply_parameters ("ReplyParameters"): Description of the message to reply to
            reply_markup (Union["InlineKeyboardMarkup", "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]): Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
        """
        response_api: objects.Message = await self.exec_request(
            "sendLocation",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "latitude": latitude,
                  "longitude": longitude,
                  "horizontal_accuracy": horizontal_accuracy,
                  "live_period": live_period,
                  "heading": heading,
                  "proximity_alert_radius": proximity_alert_radius,
                  "disable_notification": disable_notification,
                  "protect_content": protect_content,
                  "allow_paid_broadcast": allow_paid_broadcast,
                  "message_effect_id": message_effect_id,
                  "reply_parameters": reply_parameters,
                  "reply_markup": reply_markup},
            return_type=objects.Message  # type: ignore

        )
        return response_api

    async def send_venue(self, chat_id: Union[int, str], latitude: float, longitude: float, title: str, address: str, *, business_connection_id: Optional[str] = None, message_thread_id: Optional[int] = None, foursquare_id: Optional[str] = None, foursquare_type: Optional[str] = None, google_place_id: Optional[str] = None, google_place_type: Optional[str] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None, allow_paid_broadcast: Optional[bool] = None, message_effect_id: Optional[str] = None, reply_parameters: Optional[objects.ReplyParameters] = None, reply_markup: Optional[Union[objects.InlineKeyboardMarkup, objects.ReplyKeyboardMarkup, objects.ReplyKeyboardRemove, objects.ForceReply]] = None) -> objects.Message:
        """Use this method to send information about a venue. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message will be sent
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
            latitude (float): Latitude of the venue
            longitude (float): Longitude of the venue
            title (str): Name of the venue
            address (str): Address of the venue
            foursquare_id (str): Foursquare identifier of the venue
            foursquare_type (str): Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
            google_place_id (str): Google Places identifier of the venue
            google_place_type (str): Google Places type of the venue. (See [supported types](https://developers.google.com/places/web-service/supported_types).)
            disable_notification (bool): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
            protect_content (bool): Protects the contents of the sent message from forwarding and saving
            allow_paid_broadcast (bool): Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance
            message_effect_id (str): Unique identifier of the message effect to be added to the message; for private chats only
            reply_parameters ("ReplyParameters"): Description of the message to reply to
            reply_markup (Union["InlineKeyboardMarkup", "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]): Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
        """
        response_api: objects.Message = await self.exec_request(
            "sendVenue",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "latitude": latitude,
                  "longitude": longitude,
                  "title": title,
                  "address": address,
                  "foursquare_id": foursquare_id,
                  "foursquare_type": foursquare_type,
                  "google_place_id": google_place_id,
                  "google_place_type": google_place_type,
                  "disable_notification": disable_notification,
                  "protect_content": protect_content,
                  "allow_paid_broadcast": allow_paid_broadcast,
                  "message_effect_id": message_effect_id,
                  "reply_parameters": reply_parameters,
                  "reply_markup": reply_markup},
            return_type=objects.Message  # type: ignore

        )
        return response_api

    async def send_contact(self, chat_id: Union[int, str], phone_number: str, first_name: str, *, business_connection_id: Optional[str] = None, message_thread_id: Optional[int] = None, last_name: Optional[str] = None, vcard: Optional[str] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None, allow_paid_broadcast: Optional[bool] = None, message_effect_id: Optional[str] = None, reply_parameters: Optional[objects.ReplyParameters] = None, reply_markup: Optional[Union[objects.InlineKeyboardMarkup, objects.ReplyKeyboardMarkup, objects.ReplyKeyboardRemove, objects.ForceReply]] = None) -> objects.Message:
        """Use this method to send phone contacts. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message will be sent
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
            phone_number (str): Contact's phone number
            first_name (str): Contact's first name
            last_name (str): Contact's last name
            vcard (str): Additional data about the contact in the form of a [vCard](https://en.wikipedia.org/wiki/VCard), 0-2048 bytes
            disable_notification (bool): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
            protect_content (bool): Protects the contents of the sent message from forwarding and saving
            allow_paid_broadcast (bool): Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance
            message_effect_id (str): Unique identifier of the message effect to be added to the message; for private chats only
            reply_parameters ("ReplyParameters"): Description of the message to reply to
            reply_markup (Union["InlineKeyboardMarkup", "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]): Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
        """
        response_api: objects.Message = await self.exec_request(
            "sendContact",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "phone_number": phone_number,
                  "first_name": first_name,
                  "last_name": last_name,
                  "vcard": vcard,
                  "disable_notification": disable_notification,
                  "protect_content": protect_content,
                  "allow_paid_broadcast": allow_paid_broadcast,
                  "message_effect_id": message_effect_id,
                  "reply_parameters": reply_parameters,
                  "reply_markup": reply_markup},
            return_type=objects.Message  # type: ignore

        )
        return response_api

    async def send_poll(self, chat_id: Union[int, str], question: str, options: List[objects.InputPollOption], *, business_connection_id: Optional[str] = None, message_thread_id: Optional[int] = None, question_parse_mode: Optional[str] = None, question_entities: Optional[List[objects.MessageEntity]] = None, is_anonymous: Optional[bool] = None, type_: Optional[str] = None, allows_multiple_answers: Optional[bool] = None, correct_option_id: Optional[int] = None, explanation: Optional[str] = None, explanation_parse_mode: Optional[str] = None, explanation_entities: Optional[List[objects.MessageEntity]] = None, open_period: Optional[int] = None, close_date: Optional[int] = None, is_closed: Optional[bool] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None, allow_paid_broadcast: Optional[bool] = None, message_effect_id: Optional[str] = None, reply_parameters: Optional[objects.ReplyParameters] = None, reply_markup: Optional[Union[objects.InlineKeyboardMarkup, objects.ReplyKeyboardMarkup, objects.ReplyKeyboardRemove, objects.ForceReply]] = None) -> objects.Message:
        """Use this method to send a native poll. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message will be sent
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
            question (str): Poll question, 1-300 characters
            question_parse_mode (str): Mode for parsing entities in the question. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. Currently, only custom emoji entities are allowed
            question_entities (List["MessageEntity"]): A JSON-serialized list of special entities that appear in the poll question. It can be specified instead of *question_parse_mode*
            options (List["InputPollOption"]): A JSON-serialized list of 2-10 answer options
            is_anonymous (bool): *True*, if the poll needs to be anonymous, defaults to *True*
            type_ (str): Poll type, “quiz” or “regular”, defaults to “regular”
            allows_multiple_answers (bool): *True*, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to *False*
            correct_option_id (int): 0-based identifier of the correct answer option, required for polls in quiz mode
            explanation (str): Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing
            explanation_parse_mode (str): Mode for parsing entities in the explanation. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
            explanation_entities (List["MessageEntity"]): A JSON-serialized list of special entities that appear in the poll explanation. It can be specified instead of *explanation_parse_mode*
            open_period (int): Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with *close_date*.
            close_date (int): Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future. Can't be used together with *open_period*.
            is_closed (bool): Pass *True* if the poll needs to be immediately closed. This can be useful for poll preview.
            disable_notification (bool): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
            protect_content (bool): Protects the contents of the sent message from forwarding and saving
            allow_paid_broadcast (bool): Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance
            message_effect_id (str): Unique identifier of the message effect to be added to the message; for private chats only
            reply_parameters ("ReplyParameters"): Description of the message to reply to
            reply_markup (Union["InlineKeyboardMarkup", "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]): Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
        """
        response_api: objects.Message = await self.exec_request(
            "sendPoll",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "question": question,
                  "question_parse_mode": question_parse_mode,
                  "question_entities": question_entities,
                  "options": options,
                  "is_anonymous": is_anonymous,
                  "type": type_,
                  "allows_multiple_answers": allows_multiple_answers,
                  "correct_option_id": correct_option_id,
                  "explanation": explanation,
                  "explanation_parse_mode": explanation_parse_mode,
                  "explanation_entities": explanation_entities,
                  "open_period": open_period,
                  "close_date": close_date,
                  "is_closed": is_closed,
                  "disable_notification": disable_notification,
                  "protect_content": protect_content,
                  "allow_paid_broadcast": allow_paid_broadcast,
                  "message_effect_id": message_effect_id,
                  "reply_parameters": reply_parameters,
                  "reply_markup": reply_markup},
            return_type=objects.Message  # type: ignore

        )
        return response_api

    async def send_dice(self, chat_id: Union[int, str], *, business_connection_id: Optional[str] = None, message_thread_id: Optional[int] = None, emoji: Optional[str] = "🎲", disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None, allow_paid_broadcast: Optional[bool] = None, message_effect_id: Optional[str] = None, reply_parameters: Optional[objects.ReplyParameters] = None, reply_markup: Optional[Union[objects.InlineKeyboardMarkup, objects.ReplyKeyboardMarkup, objects.ReplyKeyboardRemove, objects.ForceReply]] = None) -> objects.Message:
        """Use this method to send an animated emoji that will display a random value. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message will be sent
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
            emoji (str): Emoji on which the dice throw animation is based. Currently, must be one of “🎲”, “🎯”, “🏀”, “⚽”, “🎳”, or “🎰”. Dice can have values 1-6 for “🎲”, “🎯” and “🎳”, values 1-5 for “🏀” and “⚽”, and values 1-64 for “🎰”. Defaults to “🎲”
            disable_notification (bool): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
            protect_content (bool): Protects the contents of the sent message from forwarding
            allow_paid_broadcast (bool): Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance
            message_effect_id (str): Unique identifier of the message effect to be added to the message; for private chats only
            reply_parameters ("ReplyParameters"): Description of the message to reply to
            reply_markup (Union["InlineKeyboardMarkup", "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]): Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
        """
        response_api: objects.Message = await self.exec_request(
            "sendDice",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "emoji": emoji,
                  "disable_notification": disable_notification,
                  "protect_content": protect_content,
                  "allow_paid_broadcast": allow_paid_broadcast,
                  "message_effect_id": message_effect_id,
                  "reply_parameters": reply_parameters,
                  "reply_markup": reply_markup},
            return_type=objects.Message  # type: ignore

        )
        return response_api

    async def send_chat_action(self, chat_id: Union[int, str], action: str, *, business_connection_id: Optional[str] = None, message_thread_id: Optional[int] = None) -> bool:
        """Use this method when you need to tell the user that something is happening on the bot's side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Returns *True* on success.

Example: The [ImageBot](https://t.me/imagebot) needs some time to process a request and upload the image. Instead of sending a text message along the lines of “Retrieving image, please wait…”, the bot may use [sendChatAction](https://core.telegram.org/bots/api/#sendchataction) with *action* = *upload_photo*. The user will see a “sending photo” status for the bot.

We only recommend using this method when a response from the bot will take a **noticeable** amount of time to arrive.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the action will be sent
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_thread_id (int): Unique identifier for the target message thread; for supergroups only
            action (str): Type of action to broadcast. Choose one, depending on what the user is about to receive: *typing* for [text messages](https://core.telegram.org/bots/api/#sendmessage), *upload_photo* for [photos](https://core.telegram.org/bots/api/#sendphoto), *record_video* or *upload_video* for [videos](https://core.telegram.org/bots/api/#sendvideo), *record_voice* or *upload_voice* for [voice notes](https://core.telegram.org/bots/api/#sendvoice), *upload_document* for [general files](https://core.telegram.org/bots/api/#senddocument), *choose_sticker* for [stickers](https://core.telegram.org/bots/api/#sendsticker), *find_location* for [location data](https://core.telegram.org/bots/api/#sendlocation), *record_video_note* or *upload_video_note* for [video notes](https://core.telegram.org/bots/api/#sendvideonote).
        """
        response_api: bool = await self.exec_request(
            "sendChatAction",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "action": action},
            return_type=bool  # type: ignore

        )
        return response_api

    async def set_message_reaction(self, chat_id: Union[int, str], message_id: int, *, reaction: Optional[List[objects.ReactionType]] = None, is_big: Optional[bool] = None) -> bool:
        """Use this method to change the chosen reactions on a message. Service messages of some types can't be reacted to. Automatically forwarded messages from a channel to its discussion group have the same available reactions as messages in the channel. Bots can't use paid reactions. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_id (int): Identifier of the target message. If the message belongs to a media group, the reaction is set to the first non-deleted message in the group instead.
            reaction (List["ReactionType"]): A JSON-serialized list of reaction types to set on the message. Currently, as non-premium users, bots can set up to one reaction per message. A custom emoji reaction can be used if it is either already present on the message or explicitly allowed by chat administrators. Paid reactions can't be used by bots.
            is_big (bool): Pass *True* to set the reaction with a big animation
        """
        response_api: bool = await self.exec_request(
            "setMessageReaction",
            json={"chat_id": chat_id,
                  "message_id": message_id,
                  "reaction": reaction,
                  "is_big": is_big},
            return_type=bool  # type: ignore

        )
        return response_api

    async def get_user_profile_photos(self, user_id: int, *, offset: Optional[int] = None, limit: Optional[int] = 100) -> objects.UserProfilePhotos:
        """Use this method to get a list of profile pictures for a user. Returns a [UserProfilePhotos](https://core.telegram.org/bots/api/#userprofilephotos) object.

        Args:
            user_id (int): Unique identifier of the target user
            offset (int): Sequential number of the first photo to be returned. By default, all photos are returned.
            limit (int): Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to 100.
        """
        response_api: objects.UserProfilePhotos = await self.exec_request(
            "getUserProfilePhotos",
            json={"user_id": user_id,
                  "offset": offset,
                  "limit": limit},
            return_type=objects.UserProfilePhotos  # type: ignore

        )
        return response_api

    async def set_user_emoji_status(self, user_id: int, *, emoji_status_custom_emoji_id: Optional[str] = None, emoji_status_expiration_date: Optional[int] = None) -> bool:
        """Changes the emoji status for a given user that previously allowed the bot to manage their emoji status via the Mini App method [requestEmojiStatusAccess](https://core.telegram.org/bots/webapps#initializing-mini-apps). Returns *True* on success.

        Args:
            user_id (int): Unique identifier of the target user
            emoji_status_custom_emoji_id (str): Custom emoji identifier of the emoji status to set. Pass an empty string to remove the status.
            emoji_status_expiration_date (int): Expiration date of the emoji status, if any
        """
        response_api: bool = await self.exec_request(
            "setUserEmojiStatus",
            json={"user_id": user_id,
                  "emoji_status_custom_emoji_id": emoji_status_custom_emoji_id,
                  "emoji_status_expiration_date": emoji_status_expiration_date},
            return_type=bool  # type: ignore

        )
        return response_api

    async def get_file(self, file_id: str) -> objects.File:
        """Use this method to get basic information about a file and prepare it for downloading. For the moment, bots can download files of up to 20MB in size. On success, a [File](https://core.telegram.org/bots/api/#file) object is returned. The file can then be downloaded via the link `https://api.telegram.org/file/bot<token>/<file_path>`, where `<file_path>` is taken from the response. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling [getFile](https://core.telegram.org/bots/api/#getfile) again.

        Args:
            file_id (str): File identifier to get information about
        """
        response_api: objects.File = await self.exec_request(
            "getFile",
            json={"file_id": file_id},
            return_type=objects.File  # type: ignore

        )
        return response_api

    async def ban_chat_member(self, chat_id: Union[int, str], user_id: int, *, until_date: Optional[int] = None, revoke_messages: Optional[bool] = None) -> bool:
        """Use this method to ban a user in a group, a supergroup or a channel. In the case of supergroups and channels, the user will not be able to return to the chat on their own using invite links, etc., unless [unbanned](https://core.telegram.org/bots/api/#unbanchatmember) first. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target group or username of the target supergroup or channel (in the format `@channelusername`)
            user_id (int): Unique identifier of the target user
            until_date (int): Date when the user will be unbanned; Unix time. If user is banned for more than 366 days or less than 30 seconds from the current time they are considered to be banned forever. Applied for supergroups and channels only.
            revoke_messages (bool): Pass *True* to delete all messages from the chat for the user that is being removed. If *False*, the user will be able to see messages in the group that were sent before the user was removed. Always *True* for supergroups and channels.
        """
        response_api: bool = await self.exec_request(
            "banChatMember",
            json={"chat_id": chat_id,
                  "user_id": user_id,
                  "until_date": until_date,
                  "revoke_messages": revoke_messages},
            return_type=bool  # type: ignore

        )
        return response_api

    async def unban_chat_member(self, chat_id: Union[int, str], user_id: int, *, only_if_banned: Optional[bool] = None) -> bool:
        """Use this method to unban a previously banned user in a supergroup or channel. The user will **not** return to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator for this to work. By default, this method guarantees that after the call the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat they will also be **removed** from the chat. If you don't want this, use the parameter *only_if_banned*. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target group or username of the target supergroup or channel (in the format `@channelusername`)
            user_id (int): Unique identifier of the target user
            only_if_banned (bool): Do nothing if the user is not banned
        """
        response_api: bool = await self.exec_request(
            "unbanChatMember",
            json={"chat_id": chat_id,
                  "user_id": user_id,
                  "only_if_banned": only_if_banned},
            return_type=bool  # type: ignore

        )
        return response_api

    async def restrict_chat_member(self, chat_id: Union[int, str], user_id: int, permissions: objects.ChatPermissions, *, use_independent_chat_permissions: Optional[bool] = None, until_date: Optional[int] = None) -> bool:
        """Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate administrator rights. Pass *True* for all permissions to lift restrictions from a user. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)
            user_id (int): Unique identifier of the target user
            permissions ("ChatPermissions"): A JSON-serialized object for new user permissions
            use_independent_chat_permissions (bool): Pass *True* if chat permissions are set independently. Otherwise, the *can_send_other_messages* and *can_add_web_page_previews* permissions will imply the *can_send_messages*, *can_send_audios*, *can_send_documents*, *can_send_photos*, *can_send_videos*, *can_send_video_notes*, and *can_send_voice_notes* permissions; the *can_send_polls* permission will imply the *can_send_messages* permission.
            until_date (int): Date when restrictions will be lifted for the user; Unix time. If user is restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be restricted forever
        """
        response_api: bool = await self.exec_request(
            "restrictChatMember",
            json={"chat_id": chat_id,
                  "user_id": user_id,
                  "permissions": permissions,
                  "use_independent_chat_permissions": use_independent_chat_permissions,
                  "until_date": until_date},
            return_type=bool  # type: ignore

        )
        return response_api

    async def promote_chat_member(self, chat_id: Union[int, str], user_id: int, *, is_anonymous: Optional[bool] = None, can_manage_chat: Optional[bool] = None, can_delete_messages: Optional[bool] = None, can_manage_video_chats: Optional[bool] = None, can_restrict_members: Optional[bool] = None, can_promote_members: Optional[bool] = None, can_change_info: Optional[bool] = None, can_invite_users: Optional[bool] = None, can_post_stories: Optional[bool] = None, can_edit_stories: Optional[bool] = None, can_delete_stories: Optional[bool] = None, can_post_messages: Optional[bool] = None, can_edit_messages: Optional[bool] = None, can_pin_messages: Optional[bool] = None, can_manage_topics: Optional[bool] = None) -> bool:
        """Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Pass *False* for all boolean parameters to demote a user. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            user_id (int): Unique identifier of the target user
            is_anonymous (bool): Pass *True* if the administrator's presence in the chat is hidden
            can_manage_chat (bool): Pass *True* if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages and ignore slow mode. Implied by any other administrator privilege.
            can_delete_messages (bool): Pass *True* if the administrator can delete messages of other users
            can_manage_video_chats (bool): Pass *True* if the administrator can manage video chats
            can_restrict_members (bool): Pass *True* if the administrator can restrict, ban or unban chat members, or access supergroup statistics
            can_promote_members (bool): Pass *True* if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by him)
            can_change_info (bool): Pass *True* if the administrator can change chat title, photo and other settings
            can_invite_users (bool): Pass *True* if the administrator can invite new users to the chat
            can_post_stories (bool): Pass *True* if the administrator can post stories to the chat
            can_edit_stories (bool): Pass *True* if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat's story archive
            can_delete_stories (bool): Pass *True* if the administrator can delete stories posted by other users
            can_post_messages (bool): Pass *True* if the administrator can post messages in the channel, or access channel statistics; for channels only
            can_edit_messages (bool): Pass *True* if the administrator can edit messages of other users and can pin messages; for channels only
            can_pin_messages (bool): Pass *True* if the administrator can pin messages; for supergroups only
            can_manage_topics (bool): Pass *True* if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only
        """
        response_api: bool = await self.exec_request(
            "promoteChatMember",
            json={"chat_id": chat_id,
                  "user_id": user_id,
                  "is_anonymous": is_anonymous,
                  "can_manage_chat": can_manage_chat,
                  "can_delete_messages": can_delete_messages,
                  "can_manage_video_chats": can_manage_video_chats,
                  "can_restrict_members": can_restrict_members,
                  "can_promote_members": can_promote_members,
                  "can_change_info": can_change_info,
                  "can_invite_users": can_invite_users,
                  "can_post_stories": can_post_stories,
                  "can_edit_stories": can_edit_stories,
                  "can_delete_stories": can_delete_stories,
                  "can_post_messages": can_post_messages,
                  "can_edit_messages": can_edit_messages,
                  "can_pin_messages": can_pin_messages,
                  "can_manage_topics": can_manage_topics},
            return_type=bool  # type: ignore

        )
        return response_api

    async def set_chat_administrator_custom_title(self, chat_id: Union[int, str], user_id: int, custom_title: str) -> bool:
        """Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)
            user_id (int): Unique identifier of the target user
            custom_title (str): New custom title for the administrator; 0-16 characters, emoji are not allowed
        """
        response_api: bool = await self.exec_request(
            "setChatAdministratorCustomTitle",
            json={"chat_id": chat_id,
                  "user_id": user_id,
                  "custom_title": custom_title},
            return_type=bool  # type: ignore

        )
        return response_api

    async def ban_chat_sender_chat(self, chat_id: Union[int, str], sender_chat_id: int) -> bool:
        """Use this method to ban a channel chat in a supergroup or a channel. Until the chat is [unbanned](https://core.telegram.org/bots/api/#unbanchatsenderchat), the owner of the banned chat won't be able to send messages on behalf of **any of their channels**. The bot must be an administrator in the supergroup or channel for this to work and must have the appropriate administrator rights. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            sender_chat_id (int): Unique identifier of the target sender chat
        """
        response_api: bool = await self.exec_request(
            "banChatSenderChat",
            json={"chat_id": chat_id,
                  "sender_chat_id": sender_chat_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def unban_chat_sender_chat(self, chat_id: Union[int, str], sender_chat_id: int) -> bool:
        """Use this method to unban a previously banned channel chat in a supergroup or channel. The bot must be an administrator for this to work and must have the appropriate administrator rights. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            sender_chat_id (int): Unique identifier of the target sender chat
        """
        response_api: bool = await self.exec_request(
            "unbanChatSenderChat",
            json={"chat_id": chat_id,
                  "sender_chat_id": sender_chat_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def set_chat_permissions(self, chat_id: Union[int, str], permissions: objects.ChatPermissions, *, use_independent_chat_permissions: Optional[bool] = None) -> bool:
        """Use this method to set default chat permissions for all members. The bot must be an administrator in the group or a supergroup for this to work and must have the *can_restrict_members* administrator rights. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)
            permissions ("ChatPermissions"): A JSON-serialized object for new default chat permissions
            use_independent_chat_permissions (bool): Pass *True* if chat permissions are set independently. Otherwise, the *can_send_other_messages* and *can_add_web_page_previews* permissions will imply the *can_send_messages*, *can_send_audios*, *can_send_documents*, *can_send_photos*, *can_send_videos*, *can_send_video_notes*, and *can_send_voice_notes* permissions; the *can_send_polls* permission will imply the *can_send_messages* permission.
        """
        response_api: bool = await self.exec_request(
            "setChatPermissions",
            json={"chat_id": chat_id,
                  "permissions": permissions,
                  "use_independent_chat_permissions": use_independent_chat_permissions},
            return_type=bool  # type: ignore

        )
        return response_api

    async def export_chat_invite_link(self, chat_id: Union[int, str]) -> str:
        """Use this method to generate a new primary invite link for a chat; any previously generated primary link is revoked. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the new invite link as *String* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
        """
        response_api: str = await self.exec_request(
            "exportChatInviteLink",
            json={"chat_id": chat_id},
            return_type=str  # type: ignore

        )
        return response_api

    async def create_chat_invite_link(self, chat_id: Union[int, str], *, name: Optional[str] = None, expire_date: Optional[int] = None, member_limit: Optional[int] = None, creates_join_request: Optional[bool] = None) -> objects.ChatInviteLink:
        """Use this method to create an additional invite link for a chat. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. The link can be revoked using the method [revokeChatInviteLink](https://core.telegram.org/bots/api/#revokechatinvitelink). Returns the new invite link as [ChatInviteLink](https://core.telegram.org/bots/api/#chatinvitelink) object.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            name (str): Invite link name; 0-32 characters
            expire_date (int): Point in time (Unix timestamp) when the link will expire
            member_limit (int): The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999
            creates_join_request (bool): *True*, if users joining the chat via the link need to be approved by chat administrators. If *True*, *member_limit* can't be specified
        """
        response_api: objects.ChatInviteLink = await self.exec_request(
            "createChatInviteLink",
            json={"chat_id": chat_id,
                  "name": name,
                  "expire_date": expire_date,
                  "member_limit": member_limit,
                  "creates_join_request": creates_join_request},
            return_type=objects.ChatInviteLink  # type: ignore

        )
        return response_api

    async def edit_chat_invite_link(self, chat_id: Union[int, str], invite_link: str, *, name: Optional[str] = None, expire_date: Optional[int] = None, member_limit: Optional[int] = None, creates_join_request: Optional[bool] = None) -> objects.ChatInviteLink:
        """Use this method to edit a non-primary invite link created by the bot. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the edited invite link as a [ChatInviteLink](https://core.telegram.org/bots/api/#chatinvitelink) object.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            invite_link (str): The invite link to edit
            name (str): Invite link name; 0-32 characters
            expire_date (int): Point in time (Unix timestamp) when the link will expire
            member_limit (int): The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999
            creates_join_request (bool): *True*, if users joining the chat via the link need to be approved by chat administrators. If *True*, *member_limit* can't be specified
        """
        response_api: objects.ChatInviteLink = await self.exec_request(
            "editChatInviteLink",
            json={"chat_id": chat_id,
                  "invite_link": invite_link,
                  "name": name,
                  "expire_date": expire_date,
                  "member_limit": member_limit,
                  "creates_join_request": creates_join_request},
            return_type=objects.ChatInviteLink  # type: ignore

        )
        return response_api

    async def create_chat_subscription_invite_link(self, chat_id: Union[int, str], subscription_period: int, subscription_price: int, *, name: Optional[str] = None) -> objects.ChatInviteLink:
        """Use this method to create a [subscription invite link](https://telegram.org/blog/superchannels-star-reactions-subscriptions#star-subscriptions) for a channel chat. The bot must have the *can_invite_users* administrator rights. The link can be edited using the method [editChatSubscriptionInviteLink](https://core.telegram.org/bots/api/#editchatsubscriptioninvitelink) or revoked using the method [revokeChatInviteLink](https://core.telegram.org/bots/api/#revokechatinvitelink). Returns the new invite link as a [ChatInviteLink](https://core.telegram.org/bots/api/#chatinvitelink) object.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target channel chat or username of the target channel (in the format `@channelusername`)
            name (str): Invite link name; 0-32 characters
            subscription_period (int): The number of seconds the subscription will be active for before the next payment. Currently, it must always be 2592000 (30 days).
            subscription_price (int): The amount of Telegram Stars a user must pay initially and after each subsequent subscription period to be a member of the chat; 1-2500
        """
        response_api: objects.ChatInviteLink = await self.exec_request(
            "createChatSubscriptionInviteLink",
            json={"chat_id": chat_id,
                  "name": name,
                  "subscription_period": subscription_period,
                  "subscription_price": subscription_price},
            return_type=objects.ChatInviteLink  # type: ignore

        )
        return response_api

    async def edit_chat_subscription_invite_link(self, chat_id: Union[int, str], invite_link: str, *, name: Optional[str] = None) -> objects.ChatInviteLink:
        """Use this method to edit a subscription invite link created by the bot. The bot must have the *can_invite_users* administrator rights. Returns the edited invite link as a [ChatInviteLink](https://core.telegram.org/bots/api/#chatinvitelink) object.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            invite_link (str): The invite link to edit
            name (str): Invite link name; 0-32 characters
        """
        response_api: objects.ChatInviteLink = await self.exec_request(
            "editChatSubscriptionInviteLink",
            json={"chat_id": chat_id,
                  "invite_link": invite_link,
                  "name": name},
            return_type=objects.ChatInviteLink  # type: ignore

        )
        return response_api

    async def revoke_chat_invite_link(self, chat_id: Union[int, str], invite_link: str) -> objects.ChatInviteLink:
        """Use this method to revoke an invite link created by the bot. If the primary link is revoked, a new link is automatically generated. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the revoked invite link as [ChatInviteLink](https://core.telegram.org/bots/api/#chatinvitelink) object.

        Args:
            chat_id (Union[int, str]): Unique identifier of the target chat or username of the target channel (in the format `@channelusername`)
            invite_link (str): The invite link to revoke
        """
        response_api: objects.ChatInviteLink = await self.exec_request(
            "revokeChatInviteLink",
            json={"chat_id": chat_id,
                  "invite_link": invite_link},
            return_type=objects.ChatInviteLink  # type: ignore

        )
        return response_api

    async def approve_chat_join_request(self, chat_id: Union[int, str], user_id: int) -> bool:
        """Use this method to approve a chat join request. The bot must be an administrator in the chat for this to work and must have the *can_invite_users* administrator right. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            user_id (int): Unique identifier of the target user
        """
        response_api: bool = await self.exec_request(
            "approveChatJoinRequest",
            json={"chat_id": chat_id,
                  "user_id": user_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def decline_chat_join_request(self, chat_id: Union[int, str], user_id: int) -> bool:
        """Use this method to decline a chat join request. The bot must be an administrator in the chat for this to work and must have the *can_invite_users* administrator right. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            user_id (int): Unique identifier of the target user
        """
        response_api: bool = await self.exec_request(
            "declineChatJoinRequest",
            json={"chat_id": chat_id,
                  "user_id": user_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def set_chat_photo(self, chat_id: Union[int, str], photo: objects.InputFile) -> bool:
        """Use this method to set a new profile photo for the chat. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            photo ("InputFile"): New chat photo, uploaded using multipart/form-data
        """
        response_api: bool = await self.exec_request(
            "setChatPhoto",
            json={"chat_id": chat_id,
                  "photo": photo},
            return_type=bool  # type: ignore

        )
        return response_api

    async def delete_chat_photo(self, chat_id: Union[int, str]) -> bool:
        """Use this method to delete a chat photo. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
        """
        response_api: bool = await self.exec_request(
            "deleteChatPhoto",
            json={"chat_id": chat_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def set_chat_title(self, chat_id: Union[int, str], title: str) -> bool:
        """Use this method to change the title of a chat. Titles can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            title (str): New chat title, 1-128 characters
        """
        response_api: bool = await self.exec_request(
            "setChatTitle",
            json={"chat_id": chat_id,
                  "title": title},
            return_type=bool  # type: ignore

        )
        return response_api

    async def set_chat_description(self, chat_id: Union[int, str], *, description: Optional[str] = None) -> bool:
        """Use this method to change the description of a group, a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            description (str): New chat description, 0-255 characters
        """
        response_api: bool = await self.exec_request(
            "setChatDescription",
            json={"chat_id": chat_id,
                  "description": description},
            return_type=bool  # type: ignore

        )
        return response_api

    async def pin_chat_message(self, chat_id: Union[int, str], message_id: int, *, business_connection_id: Optional[str] = None, disable_notification: Optional[bool] = None) -> bool:
        """Use this method to add a message to the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns *True* on success.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message will be pinned
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_id (int): Identifier of a message to pin
            disable_notification (bool): Pass *True* if it is not necessary to send a notification to all chat members about the new pinned message. Notifications are always disabled in channels and private chats.
        """
        response_api: bool = await self.exec_request(
            "pinChatMessage",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_id": message_id,
                  "disable_notification": disable_notification},
            return_type=bool  # type: ignore

        )
        return response_api

    async def unpin_chat_message(self, chat_id: Union[int, str], *, business_connection_id: Optional[str] = None, message_id: Optional[int] = None) -> bool:
        """Use this method to remove a message from the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns *True* on success.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message will be unpinned
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_id (int): Identifier of the message to unpin. Required if *business_connection_id* is specified. If not specified, the most recent pinned message (by sending date) will be unpinned.
        """
        response_api: bool = await self.exec_request(
            "unpinChatMessage",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_id": message_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def unpin_all_chat_messages(self, chat_id: Union[int, str]) -> bool:
        """Use this method to clear the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
        """
        response_api: bool = await self.exec_request(
            "unpinAllChatMessages",
            json={"chat_id": chat_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def leave_chat(self, chat_id: Union[int, str]) -> bool:
        """Use this method for your bot to leave a group, supergroup or channel. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup or channel (in the format `@channelusername`)
        """
        response_api: bool = await self.exec_request(
            "leaveChat",
            json={"chat_id": chat_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def get_chat(self, chat_id: Union[int, str]) -> objects.ChatFullInfo:
        """Use this method to get up-to-date information about the chat. Returns a [ChatFullInfo](https://core.telegram.org/bots/api/#chatfullinfo) object on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup or channel (in the format `@channelusername`)
        """
        response_api: objects.ChatFullInfo = await self.exec_request(
            "getChat",
            json={"chat_id": chat_id},
            return_type=objects.ChatFullInfo  # type: ignore

        )
        return response_api

    async def get_chat_administrators(self, chat_id: Union[int, str]) -> List[objects.ChatMember]:
        """Use this method to get a list of administrators in a chat, which aren't bots. Returns an Array of [ChatMember](https://core.telegram.org/bots/api/#chatmember) objects.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup or channel (in the format `@channelusername`)
        """
        response_api: List[objects.ChatMember] = await self.exec_request(
            "getChatAdministrators",
            json={"chat_id": chat_id},
            return_type=List[objects.ChatMember]  # type: ignore

        )
        return response_api

    async def get_chat_member_count(self, chat_id: Union[int, str]) -> int:
        """Use this method to get the number of members in a chat. Returns *Int* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup or channel (in the format `@channelusername`)
        """
        response_api: int = await self.exec_request(
            "getChatMemberCount",
            json={"chat_id": chat_id},
            return_type=int  # type: ignore

        )
        return response_api

    async def get_chat_member(self, chat_id: Union[int, str], user_id: int) -> objects.ChatMember:
        """Use this method to get information about a member of a chat. The method is only guaranteed to work for other users if the bot is an administrator in the chat. Returns a [ChatMember](https://core.telegram.org/bots/api/#chatmember) object on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup or channel (in the format `@channelusername`)
            user_id (int): Unique identifier of the target user
        """
        response_api: objects.ChatMember = await self.exec_request(
            "getChatMember",
            json={"chat_id": chat_id,
                  "user_id": user_id},
            return_type=objects.ChatMember  # type: ignore

        )
        return response_api

    async def set_chat_sticker_set(self, chat_id: Union[int, str], sticker_set_name: str) -> bool:
        """Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field *can_set_sticker_set* optionally returned in [getChat](https://core.telegram.org/bots/api/#getchat) requests to check if the bot can use this method. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)
            sticker_set_name (str): Name of the sticker set to be set as the group sticker set
        """
        response_api: bool = await self.exec_request(
            "setChatStickerSet",
            json={"chat_id": chat_id,
                  "sticker_set_name": sticker_set_name},
            return_type=bool  # type: ignore

        )
        return response_api

    async def delete_chat_sticker_set(self, chat_id: Union[int, str]) -> bool:
        """Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field *can_set_sticker_set* optionally returned in [getChat](https://core.telegram.org/bots/api/#getchat) requests to check if the bot can use this method. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)
        """
        response_api: bool = await self.exec_request(
            "deleteChatStickerSet",
            json={"chat_id": chat_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def get_forum_topic_icon_stickers(self) -> List[objects.Sticker]:
        """Use this method to get custom emoji stickers, which can be used as a forum topic icon by any user. Requires no parameters. Returns an Array of [Sticker](https://core.telegram.org/bots/api/#sticker) objects.

        Args:

        """
        response_api: List[objects.Sticker] = await self.exec_request(
            "getForumTopicIconStickers",
            json={},
            return_type=List[objects.Sticker]  # type: ignore

        )
        return response_api

    async def create_forum_topic(self, chat_id: Union[int, str], name: str, *, icon_color: Optional[int] = None, icon_custom_emoji_id: Optional[str] = None) -> objects.ForumTopic:
        """Use this method to create a topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the *can_manage_topics* administrator rights. Returns information about the created topic as a [ForumTopic](https://core.telegram.org/bots/api/#forumtopic) object.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)
            name (str): Topic name, 1-128 characters
            icon_color (int): Color of the topic icon in RGB format. Currently, must be one of 7322096 (0x6FB9F0), 16766590 (0xFFD67E), 13338331 (0xCB86DB), 9367192 (0x8EEE98), 16749490 (0xFF93B2), or 16478047 (0xFB6F5F)
            icon_custom_emoji_id (str): Unique identifier of the custom emoji shown as the topic icon. Use [getForumTopicIconStickers](https://core.telegram.org/bots/api/#getforumtopiciconstickers) to get all allowed custom emoji identifiers.
        """
        response_api: objects.ForumTopic = await self.exec_request(
            "createForumTopic",
            json={"chat_id": chat_id,
                  "name": name,
                  "icon_color": icon_color,
                  "icon_custom_emoji_id": icon_custom_emoji_id},
            return_type=objects.ForumTopic  # type: ignore

        )
        return response_api

    async def edit_forum_topic(self, chat_id: Union[int, str], message_thread_id: int, *, name: Optional[str] = None, icon_custom_emoji_id: Optional[str] = None) -> bool:
        """Use this method to edit name and icon of a topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the *can_manage_topics* administrator rights, unless it is the creator of the topic. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)
            message_thread_id (int): Unique identifier for the target message thread of the forum topic
            name (str): New topic name, 0-128 characters. If not specified or empty, the current name of the topic will be kept
            icon_custom_emoji_id (str): New unique identifier of the custom emoji shown as the topic icon. Use [getForumTopicIconStickers](https://core.telegram.org/bots/api/#getforumtopiciconstickers) to get all allowed custom emoji identifiers. Pass an empty string to remove the icon. If not specified, the current icon will be kept
        """
        response_api: bool = await self.exec_request(
            "editForumTopic",
            json={"chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "name": name,
                  "icon_custom_emoji_id": icon_custom_emoji_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def close_forum_topic(self, chat_id: Union[int, str], message_thread_id: int) -> bool:
        """Use this method to close an open topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the *can_manage_topics* administrator rights, unless it is the creator of the topic. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)
            message_thread_id (int): Unique identifier for the target message thread of the forum topic
        """
        response_api: bool = await self.exec_request(
            "closeForumTopic",
            json={"chat_id": chat_id,
                  "message_thread_id": message_thread_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def reopen_forum_topic(self, chat_id: Union[int, str], message_thread_id: int) -> bool:
        """Use this method to reopen a closed topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the *can_manage_topics* administrator rights, unless it is the creator of the topic. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)
            message_thread_id (int): Unique identifier for the target message thread of the forum topic
        """
        response_api: bool = await self.exec_request(
            "reopenForumTopic",
            json={"chat_id": chat_id,
                  "message_thread_id": message_thread_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def delete_forum_topic(self, chat_id: Union[int, str], message_thread_id: int) -> bool:
        """Use this method to delete a forum topic along with all its messages in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the *can_delete_messages* administrator rights. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)
            message_thread_id (int): Unique identifier for the target message thread of the forum topic
        """
        response_api: bool = await self.exec_request(
            "deleteForumTopic",
            json={"chat_id": chat_id,
                  "message_thread_id": message_thread_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def unpin_all_forum_topic_messages(self, chat_id: Union[int, str], message_thread_id: int) -> bool:
        """Use this method to clear the list of pinned messages in a forum topic. The bot must be an administrator in the chat for this to work and must have the *can_pin_messages* administrator right in the supergroup. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)
            message_thread_id (int): Unique identifier for the target message thread of the forum topic
        """
        response_api: bool = await self.exec_request(
            "unpinAllForumTopicMessages",
            json={"chat_id": chat_id,
                  "message_thread_id": message_thread_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def edit_general_forum_topic(self, chat_id: Union[int, str], name: str) -> bool:
        """Use this method to edit the name of the 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the *can_manage_topics* administrator rights. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)
            name (str): New topic name, 1-128 characters
        """
        response_api: bool = await self.exec_request(
            "editGeneralForumTopic",
            json={"chat_id": chat_id,
                  "name": name},
            return_type=bool  # type: ignore

        )
        return response_api

    async def close_general_forum_topic(self, chat_id: Union[int, str]) -> bool:
        """Use this method to close an open 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the *can_manage_topics* administrator rights. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)
        """
        response_api: bool = await self.exec_request(
            "closeGeneralForumTopic",
            json={"chat_id": chat_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def reopen_general_forum_topic(self, chat_id: Union[int, str]) -> bool:
        """Use this method to reopen a closed 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the *can_manage_topics* administrator rights. The topic will be automatically unhidden if it was hidden. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)
        """
        response_api: bool = await self.exec_request(
            "reopenGeneralForumTopic",
            json={"chat_id": chat_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def hide_general_forum_topic(self, chat_id: Union[int, str]) -> bool:
        """Use this method to hide the 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the *can_manage_topics* administrator rights. The topic will be automatically closed if it was open. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)
        """
        response_api: bool = await self.exec_request(
            "hideGeneralForumTopic",
            json={"chat_id": chat_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def unhide_general_forum_topic(self, chat_id: Union[int, str]) -> bool:
        """Use this method to unhide the 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the *can_manage_topics* administrator rights. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)
        """
        response_api: bool = await self.exec_request(
            "unhideGeneralForumTopic",
            json={"chat_id": chat_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def unpin_all_general_forum_topic_messages(self, chat_id: Union[int, str]) -> bool:
        """Use this method to clear the list of pinned messages in a General forum topic. The bot must be an administrator in the chat for this to work and must have the *can_pin_messages* administrator right in the supergroup. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)
        """
        response_api: bool = await self.exec_request(
            "unpinAllGeneralForumTopicMessages",
            json={"chat_id": chat_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def answer_callback_query(self, callback_query_id: str, *, text: Optional[str] = None, show_alert: Optional[bool] = None, url: Optional[str] = None, cache_time: Optional[int] = None) -> bool:
        """Use this method to send answers to callback queries sent from [inline keyboards](https://core.telegram.org/bots/features#inline-keyboards). The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, *True* is returned.

Alternatively, the user can be redirected to the specified Game URL. For this option to work, you must first create a game for your bot via [@BotFather](https://t.me/botfather) and accept the terms. Otherwise, you may use links like `t.me/your_bot?start=XXXX` that open your bot with a parameter.

        Args:
            callback_query_id (str): Unique identifier for the query to be answered
            text (str): Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters
            show_alert (bool): If *True*, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to *false*.
            url (str): URL that will be opened by the user's client. If you have created a [Game](https://core.telegram.org/bots/api/#game) and accepted the conditions via [@BotFather](https://t.me/botfather), specify the URL that opens your game - note that this will only work if the query comes from a [*callback_game*](https://core.telegram.org/bots/api/#inlinekeyboardbutton) button.  

Otherwise, you may use links like `t.me/your_bot?start=XXXX` that open your bot with a parameter.
            cache_time (int): The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching starting in version 3.14. Defaults to 0.
        """
        response_api: bool = await self.exec_request(
            "answerCallbackQuery",
            json={"callback_query_id": callback_query_id,
                  "text": text,
                  "show_alert": show_alert,
                  "url": url,
                  "cache_time": cache_time},
            return_type=bool  # type: ignore

        )
        return response_api

    async def get_user_chat_boosts(self, chat_id: Union[int, str], user_id: int) -> objects.UserChatBoosts:
        """Use this method to get the list of boosts added to a chat by a user. Requires administrator rights in the chat. Returns a [UserChatBoosts](https://core.telegram.org/bots/api/#userchatboosts) object.

        Args:
            chat_id (Union[int, str]): Unique identifier for the chat or username of the channel (in the format `@channelusername`)
            user_id (int): Unique identifier of the target user
        """
        response_api: objects.UserChatBoosts = await self.exec_request(
            "getUserChatBoosts",
            json={"chat_id": chat_id,
                  "user_id": user_id},
            return_type=objects.UserChatBoosts  # type: ignore

        )
        return response_api

    async def get_business_connection(self, business_connection_id: str) -> objects.BusinessConnection:
        """Use this method to get information about the connection of the bot with a business account. Returns a [BusinessConnection](https://core.telegram.org/bots/api/#businessconnection) object on success.

        Args:
            business_connection_id (str): Unique identifier of the business connection
        """
        response_api: objects.BusinessConnection = await self.exec_request(
            "getBusinessConnection",
            json={"business_connection_id": business_connection_id},
            return_type=objects.BusinessConnection  # type: ignore

        )
        return response_api

    async def set_my_commands(self, commands: List[objects.BotCommand], *, scope: Optional[objects.BotCommandScope] = None, language_code: Optional[str] = None) -> bool:
        """Use this method to change the list of the bot's commands. See [this manual](https://core.telegram.org/bots/features#commands) for more details about bot commands. Returns *True* on success.

        Args:
            commands (List["BotCommand"]): A JSON-serialized list of bot commands to be set as the list of the bot's commands. At most 100 commands can be specified.
            scope ("BotCommandScope"): A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to [BotCommandScopeDefault](https://core.telegram.org/bots/api/#botcommandscopedefault).
            language_code (str): A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands
        """
        response_api: bool = await self.exec_request(
            "setMyCommands",
            json={"commands": commands,
                  "scope": scope,
                  "language_code": language_code},
            return_type=bool  # type: ignore

        )
        return response_api

    async def delete_my_commands(self, *, scope: Optional[objects.BotCommandScope] = None, language_code: Optional[str] = None) -> bool:
        """Use this method to delete the list of the bot's commands for the given scope and user language. After deletion, [higher level commands](https://core.telegram.org/bots/api/#determining-list-of-commands) will be shown to affected users. Returns *True* on success.

        Args:
            scope ("BotCommandScope"): A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to [BotCommandScopeDefault](https://core.telegram.org/bots/api/#botcommandscopedefault).
            language_code (str): A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands
        """
        response_api: bool = await self.exec_request(
            "deleteMyCommands",
            json={"scope": scope,
                  "language_code": language_code},
            return_type=bool  # type: ignore

        )
        return response_api

    async def get_my_commands(self, *, scope: Optional[objects.BotCommandScope] = None, language_code: Optional[str] = None) -> List[objects.BotCommand]:
        """Use this method to get the current list of the bot's commands for the given scope and user language. Returns an Array of [BotCommand](https://core.telegram.org/bots/api/#botcommand) objects. If commands aren't set, an empty list is returned.

        Args:
            scope ("BotCommandScope"): A JSON-serialized object, describing scope of users. Defaults to [BotCommandScopeDefault](https://core.telegram.org/bots/api/#botcommandscopedefault).
            language_code (str): A two-letter ISO 639-1 language code or an empty string
        """
        response_api: List[objects.BotCommand] = await self.exec_request(
            "getMyCommands",
            json={"scope": scope,
                  "language_code": language_code},
            return_type=List[objects.BotCommand]  # type: ignore

        )
        return response_api

    async def set_my_name(self, *, name: Optional[str] = None, language_code: Optional[str] = None) -> bool:
        """Use this method to change the bot's name. Returns *True* on success.

        Args:
            name (str): New bot name; 0-64 characters. Pass an empty string to remove the dedicated name for the given language.
            language_code (str): A two-letter ISO 639-1 language code. If empty, the name will be shown to all users for whose language there is no dedicated name.
        """
        response_api: bool = await self.exec_request(
            "setMyName",
            json={"name": name,
                  "language_code": language_code},
            return_type=bool  # type: ignore

        )
        return response_api

    async def get_my_name(self, *, language_code: Optional[str] = None) -> objects.BotName:
        """Use this method to get the current bot name for the given user language. Returns [BotName](https://core.telegram.org/bots/api/#botname) on success.

        Args:
            language_code (str): A two-letter ISO 639-1 language code or an empty string
        """
        response_api: objects.BotName = await self.exec_request(
            "getMyName",
            json={"language_code": language_code},
            return_type=objects.BotName  # type: ignore

        )
        return response_api

    async def set_my_description(self, *, description: Optional[str] = None, language_code: Optional[str] = None) -> bool:
        """Use this method to change the bot's description, which is shown in the chat with the bot if the chat is empty. Returns *True* on success.

        Args:
            description (str): New bot description; 0-512 characters. Pass an empty string to remove the dedicated description for the given language.
            language_code (str): A two-letter ISO 639-1 language code. If empty, the description will be applied to all users for whose language there is no dedicated description.
        """
        response_api: bool = await self.exec_request(
            "setMyDescription",
            json={"description": description,
                  "language_code": language_code},
            return_type=bool  # type: ignore

        )
        return response_api

    async def get_my_description(self, *, language_code: Optional[str] = None) -> objects.BotDescription:
        """Use this method to get the current bot description for the given user language. Returns [BotDescription](https://core.telegram.org/bots/api/#botdescription) on success.

        Args:
            language_code (str): A two-letter ISO 639-1 language code or an empty string
        """
        response_api: objects.BotDescription = await self.exec_request(
            "getMyDescription",
            json={"language_code": language_code},
            return_type=objects.BotDescription  # type: ignore

        )
        return response_api

    async def set_my_short_description(self, *, short_description: Optional[str] = None, language_code: Optional[str] = None) -> bool:
        """Use this method to change the bot's short description, which is shown on the bot's profile page and is sent together with the link when users share the bot. Returns *True* on success.

        Args:
            short_description (str): New short description for the bot; 0-120 characters. Pass an empty string to remove the dedicated short description for the given language.
            language_code (str): A two-letter ISO 639-1 language code. If empty, the short description will be applied to all users for whose language there is no dedicated short description.
        """
        response_api: bool = await self.exec_request(
            "setMyShortDescription",
            json={"short_description": short_description,
                  "language_code": language_code},
            return_type=bool  # type: ignore

        )
        return response_api

    async def get_my_short_description(self, *, language_code: Optional[str] = None) -> objects.BotShortDescription:
        """Use this method to get the current bot short description for the given user language. Returns [BotShortDescription](https://core.telegram.org/bots/api/#botshortdescription) on success.

        Args:
            language_code (str): A two-letter ISO 639-1 language code or an empty string
        """
        response_api: objects.BotShortDescription = await self.exec_request(
            "getMyShortDescription",
            json={"language_code": language_code},
            return_type=objects.BotShortDescription  # type: ignore

        )
        return response_api

    async def set_chat_menu_button(self, *, chat_id: Optional[int] = None, menu_button: Optional[objects.MenuButton] = None) -> bool:
        """Use this method to change the bot's menu button in a private chat, or the default menu button. Returns *True* on success.

        Args:
            chat_id (int): Unique identifier for the target private chat. If not specified, default bot's menu button will be changed
            menu_button ("MenuButton"): A JSON-serialized object for the bot's new menu button. Defaults to [MenuButtonDefault](https://core.telegram.org/bots/api/#menubuttondefault)
        """
        response_api: bool = await self.exec_request(
            "setChatMenuButton",
            json={"chat_id": chat_id,
                  "menu_button": menu_button},
            return_type=bool  # type: ignore

        )
        return response_api

    async def get_chat_menu_button(self, *, chat_id: Optional[int] = None) -> objects.MenuButton:
        """Use this method to get the current value of the bot's menu button in a private chat, or the default menu button. Returns [MenuButton](https://core.telegram.org/bots/api/#menubutton) on success.

        Args:
            chat_id (int): Unique identifier for the target private chat. If not specified, default bot's menu button will be returned
        """
        response_api: objects.MenuButton = await self.exec_request(
            "getChatMenuButton",
            json={"chat_id": chat_id},
            return_type=objects.MenuButton  # type: ignore

        )
        return response_api

    async def set_my_default_administrator_rights(self, *, rights: Optional[objects.ChatAdministratorRights] = None, for_channels: Optional[bool] = None) -> bool:
        """Use this method to change the default administrator rights requested by the bot when it's added as an administrator to groups or channels. These rights will be suggested to users, but they are free to modify the list before adding the bot. Returns *True* on success.

        Args:
            rights ("ChatAdministratorRights"): A JSON-serialized object describing new default administrator rights. If not specified, the default administrator rights will be cleared.
            for_channels (bool): Pass *True* to change the default administrator rights of the bot in channels. Otherwise, the default administrator rights of the bot for groups and supergroups will be changed.
        """
        response_api: bool = await self.exec_request(
            "setMyDefaultAdministratorRights",
            json={"rights": rights,
                  "for_channels": for_channels},
            return_type=bool  # type: ignore

        )
        return response_api

    async def get_my_default_administrator_rights(self, *, for_channels: Optional[bool] = None) -> objects.ChatAdministratorRights:
        """Use this method to get the current default administrator rights of the bot. Returns [ChatAdministratorRights](https://core.telegram.org/bots/api/#chatadministratorrights) on success.

        Args:
            for_channels (bool): Pass *True* to get default administrator rights of the bot in channels. Otherwise, default administrator rights of the bot for groups and supergroups will be returned.
        """
        response_api: objects.ChatAdministratorRights = await self.exec_request(
            "getMyDefaultAdministratorRights",
            json={"for_channels": for_channels},
            return_type=objects.ChatAdministratorRights  # type: ignore

        )
        return response_api

    async def edit_message_text(self, text: str, *, business_connection_id: Optional[str] = None, chat_id: Optional[Union[int, str]] = None, message_id: Optional[int] = None, inline_message_id: Optional[str] = None, parse_mode: Optional[str] = None, entities: Optional[List[objects.MessageEntity]] = None, link_preview_options: Optional[objects.LinkPreviewOptions] = None, reply_markup: Optional[objects.InlineKeyboardMarkup] = None) -> Union[objects.Message, bool]:
        """Use this method to edit text and [game](https://core.telegram.org/bots/api/#games) messages. On success, if the edited message is not an inline message, the edited [Message](https://core.telegram.org/bots/api/#message) is returned, otherwise *True* is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within **48 hours** from the time they were sent.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message to be edited was sent
            chat_id (Union[int, str]): Required if *inline_message_id* is not specified. Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_id (int): Required if *inline_message_id* is not specified. Identifier of the message to edit
            inline_message_id (str): Required if *chat_id* and *message_id* are not specified. Identifier of the inline message
            text (str): New text of the message, 1-4096 characters after entities parsing
            parse_mode (str): Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
            entities (List["MessageEntity"]): A JSON-serialized list of special entities that appear in message text, which can be specified instead of *parse_mode*
            link_preview_options ("LinkPreviewOptions"): Link preview generation options for the message
            reply_markup ("InlineKeyboardMarkup"): A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards).
        """
        response_api: Union[objects.Message, bool] = await self.exec_request(
            "editMessageText",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_id": message_id,
                  "inline_message_id": inline_message_id,
                  "text": text,
                  "parse_mode": parse_mode,
                  "entities": entities,
                  "link_preview_options": link_preview_options,
                  "reply_markup": reply_markup},
            return_type=Union[objects.Message, bool]  # type: ignore

        )
        return response_api

    async def edit_message_caption(self, *, business_connection_id: Optional[str] = None, chat_id: Optional[Union[int, str]] = None, message_id: Optional[int] = None, inline_message_id: Optional[str] = None, caption: Optional[str] = None, parse_mode: Optional[str] = None, caption_entities: Optional[List[objects.MessageEntity]] = None, show_caption_above_media: Optional[bool] = None, reply_markup: Optional[objects.InlineKeyboardMarkup] = None) -> Union[objects.Message, bool]:
        """Use this method to edit captions of messages. On success, if the edited message is not an inline message, the edited [Message](https://core.telegram.org/bots/api/#message) is returned, otherwise *True* is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within **48 hours** from the time they were sent.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message to be edited was sent
            chat_id (Union[int, str]): Required if *inline_message_id* is not specified. Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_id (int): Required if *inline_message_id* is not specified. Identifier of the message to edit
            inline_message_id (str): Required if *chat_id* and *message_id* are not specified. Identifier of the inline message
            caption (str): New caption of the message, 0-1024 characters after entities parsing
            parse_mode (str): Mode for parsing entities in the message caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
            caption_entities (List["MessageEntity"]): A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            show_caption_above_media (bool): Pass *True*, if the caption must be shown above the message media. Supported only for animation, photo and video messages.
            reply_markup ("InlineKeyboardMarkup"): A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards).
        """
        response_api: Union[objects.Message, bool] = await self.exec_request(
            "editMessageCaption",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_id": message_id,
                  "inline_message_id": inline_message_id,
                  "caption": caption,
                  "parse_mode": parse_mode,
                  "caption_entities": caption_entities,
                  "show_caption_above_media": show_caption_above_media,
                  "reply_markup": reply_markup},
            return_type=Union[objects.Message, bool]  # type: ignore

        )
        return response_api

    async def edit_message_media(self, media: objects.InputMedia, *, business_connection_id: Optional[str] = None, chat_id: Optional[Union[int, str]] = None, message_id: Optional[int] = None, inline_message_id: Optional[str] = None, reply_markup: Optional[objects.InlineKeyboardMarkup] = None) -> Union[objects.Message, bool]:
        """Use this method to edit animation, audio, document, photo, or video messages, or to add media to text messages. If a message is part of a message album, then it can be edited only to an audio for audio albums, only to a document for document albums and to a photo or a video otherwise. When an inline message is edited, a new file can't be uploaded; use a previously uploaded file via its file_id or specify a URL. On success, if the edited message is not an inline message, the edited [Message](https://core.telegram.org/bots/api/#message) is returned, otherwise *True* is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within **48 hours** from the time they were sent.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message to be edited was sent
            chat_id (Union[int, str]): Required if *inline_message_id* is not specified. Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_id (int): Required if *inline_message_id* is not specified. Identifier of the message to edit
            inline_message_id (str): Required if *chat_id* and *message_id* are not specified. Identifier of the inline message
            media ("InputMedia"): A JSON-serialized object for a new media content of the message
            reply_markup ("InlineKeyboardMarkup"): A JSON-serialized object for a new [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards).
        """
        response_api: Union[objects.Message, bool] = await self.exec_request(
            "editMessageMedia",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_id": message_id,
                  "inline_message_id": inline_message_id,
                  "media": media,
                  "reply_markup": reply_markup},
            return_type=Union[objects.Message, bool]  # type: ignore

        )
        return response_api

    async def edit_message_live_location(self, latitude: float, longitude: float, *, business_connection_id: Optional[str] = None, chat_id: Optional[Union[int, str]] = None, message_id: Optional[int] = None, inline_message_id: Optional[str] = None, live_period: Optional[int] = None, horizontal_accuracy: Optional[float] = None, heading: Optional[int] = None, proximity_alert_radius: Optional[int] = None, reply_markup: Optional[objects.InlineKeyboardMarkup] = None) -> Union[objects.Message, bool]:
        """Use this method to edit live location messages. A location can be edited until its *live_period* expires or editing is explicitly disabled by a call to [stopMessageLiveLocation](https://core.telegram.org/bots/api/#stopmessagelivelocation). On success, if the edited message is not an inline message, the edited [Message](https://core.telegram.org/bots/api/#message) is returned, otherwise *True* is returned.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message to be edited was sent
            chat_id (Union[int, str]): Required if *inline_message_id* is not specified. Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_id (int): Required if *inline_message_id* is not specified. Identifier of the message to edit
            inline_message_id (str): Required if *chat_id* and *message_id* are not specified. Identifier of the inline message
            latitude (float): Latitude of new location
            longitude (float): Longitude of new location
            live_period (int): New period in seconds during which the location can be updated, starting from the message send date. If 0x7FFFFFFF is specified, then the location can be updated forever. Otherwise, the new value must not exceed the current *live_period* by more than a day, and the live location expiration date must remain within the next 90 days. If not specified, then *live_period* remains unchanged
            horizontal_accuracy (float): The radius of uncertainty for the location, measured in meters; 0-1500
            heading (int): Direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
            proximity_alert_radius (int): The maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
            reply_markup ("InlineKeyboardMarkup"): A JSON-serialized object for a new [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards).
        """
        response_api: Union[objects.Message, bool] = await self.exec_request(
            "editMessageLiveLocation",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_id": message_id,
                  "inline_message_id": inline_message_id,
                  "latitude": latitude,
                  "longitude": longitude,
                  "live_period": live_period,
                  "horizontal_accuracy": horizontal_accuracy,
                  "heading": heading,
                  "proximity_alert_radius": proximity_alert_radius,
                  "reply_markup": reply_markup},
            return_type=Union[objects.Message, bool]  # type: ignore

        )
        return response_api

    async def stop_message_live_location(self, *, business_connection_id: Optional[str] = None, chat_id: Optional[Union[int, str]] = None, message_id: Optional[int] = None, inline_message_id: Optional[str] = None, reply_markup: Optional[objects.InlineKeyboardMarkup] = None) -> Union[objects.Message, bool]:
        """Use this method to stop updating a live location message before *live_period* expires. On success, if the message is not an inline message, the edited [Message](https://core.telegram.org/bots/api/#message) is returned, otherwise *True* is returned.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message to be edited was sent
            chat_id (Union[int, str]): Required if *inline_message_id* is not specified. Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_id (int): Required if *inline_message_id* is not specified. Identifier of the message with live location to stop
            inline_message_id (str): Required if *chat_id* and *message_id* are not specified. Identifier of the inline message
            reply_markup ("InlineKeyboardMarkup"): A JSON-serialized object for a new [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards).
        """
        response_api: Union[objects.Message, bool] = await self.exec_request(
            "stopMessageLiveLocation",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_id": message_id,
                  "inline_message_id": inline_message_id,
                  "reply_markup": reply_markup},
            return_type=Union[objects.Message, bool]  # type: ignore

        )
        return response_api

    async def edit_message_reply_markup(self, *, business_connection_id: Optional[str] = None, chat_id: Optional[Union[int, str]] = None, message_id: Optional[int] = None, inline_message_id: Optional[str] = None, reply_markup: Optional[objects.InlineKeyboardMarkup] = None) -> Union[objects.Message, bool]:
        """Use this method to edit only the reply markup of messages. On success, if the edited message is not an inline message, the edited [Message](https://core.telegram.org/bots/api/#message) is returned, otherwise *True* is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within **48 hours** from the time they were sent.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message to be edited was sent
            chat_id (Union[int, str]): Required if *inline_message_id* is not specified. Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_id (int): Required if *inline_message_id* is not specified. Identifier of the message to edit
            inline_message_id (str): Required if *chat_id* and *message_id* are not specified. Identifier of the inline message
            reply_markup ("InlineKeyboardMarkup"): A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards).
        """
        response_api: Union[objects.Message, bool] = await self.exec_request(
            "editMessageReplyMarkup",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_id": message_id,
                  "inline_message_id": inline_message_id,
                  "reply_markup": reply_markup},
            return_type=Union[objects.Message, bool]  # type: ignore

        )
        return response_api

    async def stop_poll(self, chat_id: Union[int, str], message_id: int, *, business_connection_id: Optional[str] = None, reply_markup: Optional[objects.InlineKeyboardMarkup] = None) -> objects.Poll:
        """Use this method to stop a poll which was sent by the bot. On success, the stopped [Poll](https://core.telegram.org/bots/api/#poll) is returned.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message to be edited was sent
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_id (int): Identifier of the original message with the poll
            reply_markup ("InlineKeyboardMarkup"): A JSON-serialized object for a new message [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards).
        """
        response_api: objects.Poll = await self.exec_request(
            "stopPoll",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_id": message_id,
                  "reply_markup": reply_markup},
            return_type=objects.Poll  # type: ignore

        )
        return response_api

    async def delete_message(self, chat_id: Union[int, str], message_id: int) -> bool:
        """Use this method to delete a message, including service messages, with the following limitations:  
- A message can only be deleted if it was sent less than 48 hours ago.  
- Service messages about a supergroup, channel, or forum topic creation can't be deleted.  
- A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.  
- Bots can delete outgoing messages in private chats, groups, and supergroups.  
- Bots can delete incoming messages in private chats.  
- Bots granted *can_post_messages* permissions can delete outgoing messages in channels.  
- If the bot is an administrator of a group, it can delete any message there.  
- If the bot has *can_delete_messages* permission in a supergroup or a channel, it can delete any message there.  
Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_id (int): Identifier of the message to delete
        """
        response_api: bool = await self.exec_request(
            "deleteMessage",
            json={"chat_id": chat_id,
                  "message_id": message_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def delete_messages(self, chat_id: Union[int, str], message_ids: List[int]) -> bool:
        """Use this method to delete multiple messages simultaneously. If some of the specified messages can't be found, they are skipped. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_ids (List[int]): A JSON-serialized list of 1-100 identifiers of messages to delete. See [deleteMessage](https://core.telegram.org/bots/api/#deletemessage) for limitations on which messages can be deleted
        """
        response_api: bool = await self.exec_request(
            "deleteMessages",
            json={"chat_id": chat_id,
                  "message_ids": message_ids},
            return_type=bool  # type: ignore

        )
        return response_api

    async def send_sticker(self, chat_id: Union[int, str], sticker: Union[objects.InputFile, str], *, business_connection_id: Optional[str] = None, message_thread_id: Optional[int] = None, emoji: Optional[str] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None, allow_paid_broadcast: Optional[bool] = None, message_effect_id: Optional[str] = None, reply_parameters: Optional[objects.ReplyParameters] = None, reply_markup: Optional[Union[objects.InlineKeyboardMarkup, objects.ReplyKeyboardMarkup, objects.ReplyKeyboardRemove, objects.ForceReply]] = None) -> objects.Message:
        """Use this method to send static .WEBP, [animated](https://telegram.org/blog/animated-stickers) .TGS, or [video](https://telegram.org/blog/video-stickers-better-reactions) .WEBM stickers. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message will be sent
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
            sticker (Union["InputFile", str]): Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a .WEBP sticker from the Internet, or upload a new .WEBP, .TGS, or .WEBM sticker using multipart/form-data. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files). Video and animated stickers can't be sent via an HTTP URL.
            emoji (str): Emoji associated with the sticker; only for just uploaded stickers
            disable_notification (bool): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
            protect_content (bool): Protects the contents of the sent message from forwarding and saving
            allow_paid_broadcast (bool): Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance
            message_effect_id (str): Unique identifier of the message effect to be added to the message; for private chats only
            reply_parameters ("ReplyParameters"): Description of the message to reply to
            reply_markup (Union["InlineKeyboardMarkup", "ReplyKeyboardMarkup", "ReplyKeyboardRemove", "ForceReply"]): Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
        """
        response_api: objects.Message = await self.exec_request(
            "sendSticker",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "sticker": sticker,
                  "emoji": emoji,
                  "disable_notification": disable_notification,
                  "protect_content": protect_content,
                  "allow_paid_broadcast": allow_paid_broadcast,
                  "message_effect_id": message_effect_id,
                  "reply_parameters": reply_parameters,
                  "reply_markup": reply_markup},
            return_type=objects.Message  # type: ignore

        )
        return response_api

    async def get_sticker_set(self, name: str) -> objects.StickerSet:
        """Use this method to get a sticker set. On success, a [StickerSet](https://core.telegram.org/bots/api/#stickerset) object is returned.

        Args:
            name (str): Name of the sticker set
        """
        response_api: objects.StickerSet = await self.exec_request(
            "getStickerSet",
            json={"name": name},
            return_type=objects.StickerSet  # type: ignore

        )
        return response_api

    async def get_custom_emoji_stickers(self, custom_emoji_ids: List[str]) -> List[objects.Sticker]:
        """Use this method to get information about custom emoji stickers by their identifiers. Returns an Array of [Sticker](https://core.telegram.org/bots/api/#sticker) objects.

        Args:
            custom_emoji_ids (List[str]): A JSON-serialized list of custom emoji identifiers. At most 200 custom emoji identifiers can be specified.
        """
        response_api: List[objects.Sticker] = await self.exec_request(
            "getCustomEmojiStickers",
            json={"custom_emoji_ids": custom_emoji_ids},
            return_type=List[objects.Sticker]  # type: ignore

        )
        return response_api

    async def upload_sticker_file(self, user_id: int, sticker: objects.InputFile, sticker_format: str) -> objects.File:
        """Use this method to upload a file with a sticker for later use in the [createNewStickerSet](https://core.telegram.org/bots/api/#createnewstickerset), [addStickerToSet](https://core.telegram.org/bots/api/#addstickertoset), or [replaceStickerInSet](https://core.telegram.org/bots/api/#replacestickerinset) methods (the file can be used multiple times). Returns the uploaded [File](https://core.telegram.org/bots/api/#file) on success.

        Args:
            user_id (int): User identifier of sticker file owner
            sticker ("InputFile"): A file with the sticker in .WEBP, .PNG, .TGS, or .WEBM format. See [https://core.telegram.org/stickers](https://core.telegram.org/stickers) for technical requirements. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)
            sticker_format (str): Format of the sticker, must be one of “static”, “animated”, “video”
        """
        response_api: objects.File = await self.exec_request(
            "uploadStickerFile",
            json={"user_id": user_id,
                  "sticker": sticker,
                  "sticker_format": sticker_format},
            return_type=objects.File  # type: ignore

        )
        return response_api

    async def create_new_sticker_set(self, user_id: int, name: str, title: str, stickers: List[objects.InputSticker], *, sticker_type: Optional[str] = None, needs_repainting: Optional[bool] = None) -> bool:
        """Use this method to create a new sticker set owned by a user. The bot will be able to edit the sticker set thus created. Returns *True* on success.

        Args:
            user_id (int): User identifier of created sticker set owner
            name (str): Short name of sticker set, to be used in `t.me/addstickers/` URLs (e.g., *animals*). Can contain only English letters, digits and underscores. Must begin with a letter, can't contain consecutive underscores and must end in `'_by_<bot_username>'`. `<bot_username>` is case insensitive. 1-64 characters.
            title (str): Sticker set title, 1-64 characters
            stickers (List["InputSticker"]): A JSON-serialized list of 1-50 initial stickers to be added to the sticker set
            sticker_type (str): Type of stickers in the set, pass “regular”, “mask”, or “custom_emoji”. By default, a regular sticker set is created.
            needs_repainting (bool): Pass *True* if stickers in the sticker set must be repainted to the color of text when used in messages, the accent color if used as emoji status, white on chat photos, or another appropriate color based on context; for custom emoji sticker sets only
        """
        response_api: bool = await self.exec_request(
            "createNewStickerSet",
            json={"user_id": user_id,
                  "name": name,
                  "title": title,
                  "stickers": stickers,
                  "sticker_type": sticker_type,
                  "needs_repainting": needs_repainting},
            return_type=bool  # type: ignore

        )
        return response_api

    async def add_sticker_to_set(self, user_id: int, name: str, sticker: objects.InputSticker) -> bool:
        """Use this method to add a new sticker to a set created by the bot. Emoji sticker sets can have up to 200 stickers. Other sticker sets can have up to 120 stickers. Returns *True* on success.

        Args:
            user_id (int): User identifier of sticker set owner
            name (str): Sticker set name
            sticker ("InputSticker"): A JSON-serialized object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set isn't changed.
        """
        response_api: bool = await self.exec_request(
            "addStickerToSet",
            json={"user_id": user_id,
                  "name": name,
                  "sticker": sticker},
            return_type=bool  # type: ignore

        )
        return response_api

    async def set_sticker_position_in_set(self, sticker: str, position: int) -> bool:
        """Use this method to move a sticker in a set created by the bot to a specific position. Returns *True* on success.

        Args:
            sticker (str): File identifier of the sticker
            position (int): New sticker position in the set, zero-based
        """
        response_api: bool = await self.exec_request(
            "setStickerPositionInSet",
            json={"sticker": sticker,
                  "position": position},
            return_type=bool  # type: ignore

        )
        return response_api

    async def delete_sticker_from_set(self, sticker: str) -> bool:
        """Use this method to delete a sticker from a set created by the bot. Returns *True* on success.

        Args:
            sticker (str): File identifier of the sticker
        """
        response_api: bool = await self.exec_request(
            "deleteStickerFromSet",
            json={"sticker": sticker},
            return_type=bool  # type: ignore

        )
        return response_api

    async def replace_sticker_in_set(self, user_id: int, name: str, old_sticker: str, sticker: objects.InputSticker) -> bool:
        """Use this method to replace an existing sticker in a sticker set with a new one. The method is equivalent to calling [deleteStickerFromSet](https://core.telegram.org/bots/api/#deletestickerfromset), then [addStickerToSet](https://core.telegram.org/bots/api/#addstickertoset), then [setStickerPositionInSet](https://core.telegram.org/bots/api/#setstickerpositioninset). Returns *True* on success.

        Args:
            user_id (int): User identifier of the sticker set owner
            name (str): Sticker set name
            old_sticker (str): File identifier of the replaced sticker
            sticker ("InputSticker"): A JSON-serialized object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set remains unchanged.
        """
        response_api: bool = await self.exec_request(
            "replaceStickerInSet",
            json={"user_id": user_id,
                  "name": name,
                  "old_sticker": old_sticker,
                  "sticker": sticker},
            return_type=bool  # type: ignore

        )
        return response_api

    async def set_sticker_emoji_list(self, sticker: str, emoji_list: List[str]) -> bool:
        """Use this method to change the list of emoji assigned to a regular or custom emoji sticker. The sticker must belong to a sticker set created by the bot. Returns *True* on success.

        Args:
            sticker (str): File identifier of the sticker
            emoji_list (List[str]): A JSON-serialized list of 1-20 emoji associated with the sticker
        """
        response_api: bool = await self.exec_request(
            "setStickerEmojiList",
            json={"sticker": sticker,
                  "emoji_list": emoji_list},
            return_type=bool  # type: ignore

        )
        return response_api

    async def set_sticker_keywords(self, sticker: str, *, keywords: Optional[List[str]] = None) -> bool:
        """Use this method to change search keywords assigned to a regular or custom emoji sticker. The sticker must belong to a sticker set created by the bot. Returns *True* on success.

        Args:
            sticker (str): File identifier of the sticker
            keywords (List[str]): A JSON-serialized list of 0-20 search keywords for the sticker with total length of up to 64 characters
        """
        response_api: bool = await self.exec_request(
            "setStickerKeywords",
            json={"sticker": sticker,
                  "keywords": keywords},
            return_type=bool  # type: ignore

        )
        return response_api

    async def set_sticker_mask_position(self, sticker: str, *, mask_position: Optional[objects.MaskPosition] = None) -> bool:
        """Use this method to change the [mask position](https://core.telegram.org/bots/api/#maskposition) of a mask sticker. The sticker must belong to a sticker set that was created by the bot. Returns *True* on success.

        Args:
            sticker (str): File identifier of the sticker
            mask_position ("MaskPosition"): A JSON-serialized object with the position where the mask should be placed on faces. Omit the parameter to remove the mask position.
        """
        response_api: bool = await self.exec_request(
            "setStickerMaskPosition",
            json={"sticker": sticker,
                  "mask_position": mask_position},
            return_type=bool  # type: ignore

        )
        return response_api

    async def set_sticker_set_title(self, name: str, title: str) -> bool:
        """Use this method to set the title of a created sticker set. Returns *True* on success.

        Args:
            name (str): Sticker set name
            title (str): Sticker set title, 1-64 characters
        """
        response_api: bool = await self.exec_request(
            "setStickerSetTitle",
            json={"name": name,
                  "title": title},
            return_type=bool  # type: ignore

        )
        return response_api

    async def set_sticker_set_thumbnail(self, name: str, user_id: int, format_: str, *, thumbnail: Optional[Union[objects.InputFile, str]] = None) -> bool:
        """Use this method to set the thumbnail of a regular or mask sticker set. The format of the thumbnail file must match the format of the stickers in the set. Returns *True* on success.

        Args:
            name (str): Sticker set name
            user_id (int): User identifier of the sticker set owner
            thumbnail (Union["InputFile", str]): A **.WEBP** or **.PNG** image with the thumbnail, must be up to 128 kilobytes in size and have a width and height of exactly 100px, or a **.TGS** animation with a thumbnail up to 32 kilobytes in size (see [https://core.telegram.org/stickers#animation-requirements](https://core.telegram.org/stickers#animation-requirements) for animated sticker technical requirements), or a **.WEBM** video with the thumbnail up to 32 kilobytes in size; see [https://core.telegram.org/stickers#video-requirements](https://core.telegram.org/stickers#video-requirements) for video sticker technical requirements. Pass a *file_id* as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files). Animated and video sticker set thumbnails can't be uploaded via HTTP URL. If omitted, then the thumbnail is dropped and the first sticker is used as the thumbnail.
            format_ (str): Format of the thumbnail, must be one of “static” for a **.WEBP** or **.PNG** image, “animated” for a **.TGS** animation, or “video” for a **.WEBM** video
        """
        response_api: bool = await self.exec_request(
            "setStickerSetThumbnail",
            json={"name": name,
                  "user_id": user_id,
                  "thumbnail": thumbnail,
                  "format": format_},
            return_type=bool  # type: ignore

        )
        return response_api

    async def set_custom_emoji_sticker_set_thumbnail(self, name: str, *, custom_emoji_id: Optional[str] = None) -> bool:
        """Use this method to set the thumbnail of a custom emoji sticker set. Returns *True* on success.

        Args:
            name (str): Sticker set name
            custom_emoji_id (str): Custom emoji identifier of a sticker from the sticker set; pass an empty string to drop the thumbnail and use the first sticker as the thumbnail.
        """
        response_api: bool = await self.exec_request(
            "setCustomEmojiStickerSetThumbnail",
            json={"name": name,
                  "custom_emoji_id": custom_emoji_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def delete_sticker_set(self, name: str) -> bool:
        """Use this method to delete a sticker set that was created by the bot. Returns *True* on success.

        Args:
            name (str): Sticker set name
        """
        response_api: bool = await self.exec_request(
            "deleteStickerSet",
            json={"name": name},
            return_type=bool  # type: ignore

        )
        return response_api

    async def get_available_gifts(self) -> objects.Gifts:
        """Returns the list of gifts that can be sent by the bot to users and channel chats. Requires no parameters. Returns a [Gifts](https://core.telegram.org/bots/api/#gifts) object.

        Args:

        """
        response_api: objects.Gifts = await self.exec_request(
            "getAvailableGifts",
            json={},
            return_type=objects.Gifts  # type: ignore

        )
        return response_api

    async def send_gift(self, gift_id: str, *, user_id: Optional[int] = None, chat_id: Optional[Union[int, str]] = None, pay_for_upgrade: Optional[bool] = None, text: Optional[str] = None, text_parse_mode: Optional[str] = None, text_entities: Optional[List[objects.MessageEntity]] = None) -> bool:
        """Sends a gift to the given user or channel chat. The gift can't be converted to Telegram Stars by the receiver. Returns *True* on success.

        Args:
            user_id (int): Required if *chat_id* is not specified. Unique identifier of the target user who will receive the gift.
            chat_id (Union[int, str]): Required if *user_id* is not specified. Unique identifier for the chat or username of the channel (in the format `@channelusername`) that will receive the gift.
            gift_id (str): Identifier of the gift
            pay_for_upgrade (bool): Pass *True* to pay for the gift upgrade from the bot's balance, thereby making the upgrade free for the receiver
            text (str): Text that will be shown along with the gift; 0-128 characters
            text_parse_mode (str): Mode for parsing entities in the text. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, and “custom_emoji” are ignored.
            text_entities (List["MessageEntity"]): A JSON-serialized list of special entities that appear in the gift text. It can be specified instead of *text_parse_mode*. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, and “custom_emoji” are ignored.
        """
        response_api: bool = await self.exec_request(
            "sendGift",
            json={"user_id": user_id,
                  "chat_id": chat_id,
                  "gift_id": gift_id,
                  "pay_for_upgrade": pay_for_upgrade,
                  "text": text,
                  "text_parse_mode": text_parse_mode,
                  "text_entities": text_entities},
            return_type=bool  # type: ignore

        )
        return response_api

    async def verify_user(self, user_id: int, *, custom_description: Optional[str] = None) -> bool:
        """Verifies a user [on behalf of the organization](https://telegram.org/verify#third-party-verification) which is represented by the bot. Returns *True* on success.

        Args:
            user_id (int): Unique identifier of the target user
            custom_description (str): Custom description for the verification; 0-70 characters. Must be empty if the organization isn't allowed to provide a custom verification description.
        """
        response_api: bool = await self.exec_request(
            "verifyUser",
            json={"user_id": user_id,
                  "custom_description": custom_description},
            return_type=bool  # type: ignore

        )
        return response_api

    async def verify_chat(self, chat_id: Union[int, str], *, custom_description: Optional[str] = None) -> bool:
        """Verifies a chat [on behalf of the organization](https://telegram.org/verify#third-party-verification) which is represented by the bot. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            custom_description (str): Custom description for the verification; 0-70 characters. Must be empty if the organization isn't allowed to provide a custom verification description.
        """
        response_api: bool = await self.exec_request(
            "verifyChat",
            json={"chat_id": chat_id,
                  "custom_description": custom_description},
            return_type=bool  # type: ignore

        )
        return response_api

    async def remove_user_verification(self, user_id: int) -> bool:
        """Removes verification from a user who is currently verified [on behalf of the organization](https://telegram.org/verify#third-party-verification) represented by the bot. Returns *True* on success.

        Args:
            user_id (int): Unique identifier of the target user
        """
        response_api: bool = await self.exec_request(
            "removeUserVerification",
            json={"user_id": user_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def remove_chat_verification(self, chat_id: Union[int, str]) -> bool:
        """Removes verification from a chat that is currently verified [on behalf of the organization](https://telegram.org/verify#third-party-verification) represented by the bot. Returns *True* on success.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
        """
        response_api: bool = await self.exec_request(
            "removeChatVerification",
            json={"chat_id": chat_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def answer_inline_query(self, inline_query_id: str, results: List[objects.InlineQueryResult], *, cache_time: Optional[int] = 300, is_personal: Optional[bool] = None, next_offset: Optional[str] = None, button: Optional[objects.InlineQueryResultsButton] = None) -> bool:
        """Use this method to send answers to an inline query. On success, *True* is returned.  
No more than **50** results per query are allowed.

        Args:
            inline_query_id (str): Unique identifier for the answered query
            results (List["InlineQueryResult"]): A JSON-serialized array of results for the inline query
            cache_time (int): The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300.
            is_personal (bool): Pass *True* if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query.
            next_offset (str): Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don't support pagination. Offset length can't exceed 64 bytes.
            button ("InlineQueryResultsButton"): A JSON-serialized object describing a button to be shown above inline query results
        """
        response_api: bool = await self.exec_request(
            "answerInlineQuery",
            json={"inline_query_id": inline_query_id,
                  "results": results,
                  "cache_time": cache_time,
                  "is_personal": is_personal,
                  "next_offset": next_offset,
                  "button": button},
            return_type=bool  # type: ignore

        )
        return response_api

    async def answer_web_app_query(self, web_app_query_id: str, result: objects.InlineQueryResult) -> objects.SentWebAppMessage:
        """Use this method to set the result of an interaction with a [Web App](https://core.telegram.org/bots/webapps) and send a corresponding message on behalf of the user to the chat from which the query originated. On success, a [SentWebAppMessage](https://core.telegram.org/bots/api/#sentwebappmessage) object is returned.

        Args:
            web_app_query_id (str): Unique identifier for the query to be answered
            result ("InlineQueryResult"): A JSON-serialized object describing the message to be sent
        """
        response_api: objects.SentWebAppMessage = await self.exec_request(
            "answerWebAppQuery",
            json={"web_app_query_id": web_app_query_id,
                  "result": result},
            return_type=objects.SentWebAppMessage  # type: ignore

        )
        return response_api

    async def save_prepared_inline_message(self, user_id: int, result: objects.InlineQueryResult, *, allow_user_chats: Optional[bool] = None, allow_bot_chats: Optional[bool] = None, allow_group_chats: Optional[bool] = None, allow_channel_chats: Optional[bool] = None) -> objects.PreparedInlineMessage:
        """Stores a message that can be sent by a user of a Mini App. Returns a [PreparedInlineMessage](https://core.telegram.org/bots/api/#preparedinlinemessage) object.

        Args:
            user_id (int): Unique identifier of the target user that can use the prepared message
            result ("InlineQueryResult"): A JSON-serialized object describing the message to be sent
            allow_user_chats (bool): Pass *True* if the message can be sent to private chats with users
            allow_bot_chats (bool): Pass *True* if the message can be sent to private chats with bots
            allow_group_chats (bool): Pass *True* if the message can be sent to group and supergroup chats
            allow_channel_chats (bool): Pass *True* if the message can be sent to channel chats
        """
        response_api: objects.PreparedInlineMessage = await self.exec_request(
            "savePreparedInlineMessage",
            json={"user_id": user_id,
                  "result": result,
                  "allow_user_chats": allow_user_chats,
                  "allow_bot_chats": allow_bot_chats,
                  "allow_group_chats": allow_group_chats,
                  "allow_channel_chats": allow_channel_chats},
            return_type=objects.PreparedInlineMessage  # type: ignore

        )
        return response_api

    async def send_invoice(self, chat_id: Union[int, str], title: str, description: str, payload: str, currency: str, prices: List[objects.LabeledPrice], *, message_thread_id: Optional[int] = None, provider_token: Optional[str] = None, max_tip_amount: Optional[int] = None, suggested_tip_amounts: Optional[List[int]] = None, start_parameter: Optional[str] = None, provider_data: Optional[str] = None, photo_url: Optional[str] = None, photo_size: Optional[int] = None, photo_width: Optional[int] = None, photo_height: Optional[int] = None, need_name: Optional[bool] = None, need_phone_number: Optional[bool] = None, need_email: Optional[bool] = None, need_shipping_address: Optional[bool] = None, send_phone_number_to_provider: Optional[bool] = None, send_email_to_provider: Optional[bool] = None, is_flexible: Optional[bool] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None, allow_paid_broadcast: Optional[bool] = None, message_effect_id: Optional[str] = None, reply_parameters: Optional[objects.ReplyParameters] = None, reply_markup: Optional[objects.InlineKeyboardMarkup] = None) -> objects.Message:
        """Use this method to send invoices. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
            title (str): Product name, 1-32 characters
            description (str): Product description, 1-255 characters
            payload (str): Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use it for your internal processes.
            provider_token (str): Payment provider token, obtained via [@BotFather](https://t.me/botfather). Pass an empty string for payments in [Telegram Stars](https://t.me/BotNews/90).
            currency (str): Three-letter ISO 4217 currency code, see [more on currencies](https://core.telegram.org/bots/payments#supported-currencies). Pass “XTR” for payments in [Telegram Stars](https://t.me/BotNews/90).
            prices (List["LabeledPrice"]): Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in [Telegram Stars](https://t.me/BotNews/90).
            max_tip_amount (int): The maximum accepted amount for tips in the *smallest units* of the currency (integer, **not** float/double). For example, for a maximum tip of `US$ 1.45` pass `max_tip_amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payments in [Telegram Stars](https://t.me/BotNews/90).
            suggested_tip_amounts (List[int]): A JSON-serialized array of suggested amounts of tips in the *smallest units* of the currency (integer, **not** float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed *max_tip_amount*.
            start_parameter (str): Unique deep-linking parameter. If left empty, **forwarded copies** of the sent message will have a *Pay* button, allowing multiple users to pay directly from the forwarded message, using the same invoice. If non-empty, forwarded copies of the sent message will have a *URL* button with a deep link to the bot (instead of a *Pay* button), with the value used as the start parameter
            provider_data (str): JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.
            photo_url (str): URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.
            photo_size (int): Photo size in bytes
            photo_width (int): Photo width
            photo_height (int): Photo height
            need_name (bool): Pass *True* if you require the user's full name to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90).
            need_phone_number (bool): Pass *True* if you require the user's phone number to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90).
            need_email (bool): Pass *True* if you require the user's email address to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90).
            need_shipping_address (bool): Pass *True* if you require the user's shipping address to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90).
            send_phone_number_to_provider (bool): Pass *True* if the user's phone number should be sent to the provider. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90).
            send_email_to_provider (bool): Pass *True* if the user's email address should be sent to the provider. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90).
            is_flexible (bool): Pass *True* if the final price depends on the shipping method. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90).
            disable_notification (bool): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
            protect_content (bool): Protects the contents of the sent message from forwarding and saving
            allow_paid_broadcast (bool): Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance
            message_effect_id (str): Unique identifier of the message effect to be added to the message; for private chats only
            reply_parameters ("ReplyParameters"): Description of the message to reply to
            reply_markup ("InlineKeyboardMarkup"): A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards). If empty, one 'Pay `total price`' button will be shown. If not empty, the first button must be a Pay button.
        """
        response_api: objects.Message = await self.exec_request(
            "sendInvoice",
            json={"chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "title": title,
                  "description": description,
                  "payload": payload,
                  "provider_token": provider_token,
                  "currency": currency,
                  "prices": prices,
                  "max_tip_amount": max_tip_amount,
                  "suggested_tip_amounts": suggested_tip_amounts,
                  "start_parameter": start_parameter,
                  "provider_data": provider_data,
                  "photo_url": photo_url,
                  "photo_size": photo_size,
                  "photo_width": photo_width,
                  "photo_height": photo_height,
                  "need_name": need_name,
                  "need_phone_number": need_phone_number,
                  "need_email": need_email,
                  "need_shipping_address": need_shipping_address,
                  "send_phone_number_to_provider": send_phone_number_to_provider,
                  "send_email_to_provider": send_email_to_provider,
                  "is_flexible": is_flexible,
                  "disable_notification": disable_notification,
                  "protect_content": protect_content,
                  "allow_paid_broadcast": allow_paid_broadcast,
                  "message_effect_id": message_effect_id,
                  "reply_parameters": reply_parameters,
                  "reply_markup": reply_markup},
            return_type=objects.Message  # type: ignore

        )
        return response_api

    async def create_invoice_link(self, title: str, description: str, payload: str, currency: str, prices: List[objects.LabeledPrice], *, business_connection_id: Optional[str] = None, provider_token: Optional[str] = None, subscription_period: Optional[int] = None, max_tip_amount: Optional[int] = None, suggested_tip_amounts: Optional[List[int]] = None, provider_data: Optional[str] = None, photo_url: Optional[str] = None, photo_size: Optional[int] = None, photo_width: Optional[int] = None, photo_height: Optional[int] = None, need_name: Optional[bool] = None, need_phone_number: Optional[bool] = None, need_email: Optional[bool] = None, need_shipping_address: Optional[bool] = None, send_phone_number_to_provider: Optional[bool] = None, send_email_to_provider: Optional[bool] = None, is_flexible: Optional[bool] = None) -> str:
        """Use this method to create a link for an invoice. Returns the created invoice link as *String* on success.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the link will be created. For payments in [Telegram Stars](https://t.me/BotNews/90) only.
            title (str): Product name, 1-32 characters
            description (str): Product description, 1-255 characters
            payload (str): Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use it for your internal processes.
            provider_token (str): Payment provider token, obtained via [@BotFather](https://t.me/botfather). Pass an empty string for payments in [Telegram Stars](https://t.me/BotNews/90).
            currency (str): Three-letter ISO 4217 currency code, see [more on currencies](https://core.telegram.org/bots/payments#supported-currencies). Pass “XTR” for payments in [Telegram Stars](https://t.me/BotNews/90).
            prices (List["LabeledPrice"]): Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in [Telegram Stars](https://t.me/BotNews/90).
            subscription_period (int): The number of seconds the subscription will be active for before the next payment. The currency must be set to “XTR” (Telegram Stars) if the parameter is used. Currently, it must always be 2592000 (30 days) if specified. Any number of subscriptions can be active for a given bot at the same time, including multiple concurrent subscriptions from the same user. Subscription price must no exceed 2500 Telegram Stars.
            max_tip_amount (int): The maximum accepted amount for tips in the *smallest units* of the currency (integer, **not** float/double). For example, for a maximum tip of `US$ 1.45` pass `max_tip_amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payments in [Telegram Stars](https://t.me/BotNews/90).
            suggested_tip_amounts (List[int]): A JSON-serialized array of suggested amounts of tips in the *smallest units* of the currency (integer, **not** float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed *max_tip_amount*.
            provider_data (str): JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.
            photo_url (str): URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service.
            photo_size (int): Photo size in bytes
            photo_width (int): Photo width
            photo_height (int): Photo height
            need_name (bool): Pass *True* if you require the user's full name to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90).
            need_phone_number (bool): Pass *True* if you require the user's phone number to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90).
            need_email (bool): Pass *True* if you require the user's email address to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90).
            need_shipping_address (bool): Pass *True* if you require the user's shipping address to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90).
            send_phone_number_to_provider (bool): Pass *True* if the user's phone number should be sent to the provider. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90).
            send_email_to_provider (bool): Pass *True* if the user's email address should be sent to the provider. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90).
            is_flexible (bool): Pass *True* if the final price depends on the shipping method. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90).
        """
        response_api: str = await self.exec_request(
            "createInvoiceLink",
            json={"business_connection_id": business_connection_id,
                  "title": title,
                  "description": description,
                  "payload": payload,
                  "provider_token": provider_token,
                  "currency": currency,
                  "prices": prices,
                  "subscription_period": subscription_period,
                  "max_tip_amount": max_tip_amount,
                  "suggested_tip_amounts": suggested_tip_amounts,
                  "provider_data": provider_data,
                  "photo_url": photo_url,
                  "photo_size": photo_size,
                  "photo_width": photo_width,
                  "photo_height": photo_height,
                  "need_name": need_name,
                  "need_phone_number": need_phone_number,
                  "need_email": need_email,
                  "need_shipping_address": need_shipping_address,
                  "send_phone_number_to_provider": send_phone_number_to_provider,
                  "send_email_to_provider": send_email_to_provider,
                  "is_flexible": is_flexible},
            return_type=str  # type: ignore

        )
        return response_api

    async def answer_shipping_query(self, shipping_query_id: str, ok: bool, *, shipping_options: Optional[List[objects.ShippingOption]] = None, error_message: Optional[str] = None) -> bool:
        """If you sent an invoice requesting a shipping address and the parameter *is_flexible* was specified, the Bot API will send an [Update](https://core.telegram.org/bots/api/#update) with a *shipping_query* field to the bot. Use this method to reply to shipping queries. On success, *True* is returned.

        Args:
            shipping_query_id (str): Unique identifier for the query to be answered
            ok (bool): Pass *True* if delivery to the specified address is possible and *False* if there are any problems (for example, if delivery to the specified address is not possible)
            shipping_options (List["ShippingOption"]): Required if *ok* is *True*. A JSON-serialized array of available shipping options.
            error_message (str): Required if *ok* is *False*. Error message in human readable form that explains why it is impossible to complete the order (e.g. “Sorry, delivery to your desired address is unavailable”). Telegram will display this message to the user.
        """
        response_api: bool = await self.exec_request(
            "answerShippingQuery",
            json={"shipping_query_id": shipping_query_id,
                  "ok": ok,
                  "shipping_options": shipping_options,
                  "error_message": error_message},
            return_type=bool  # type: ignore

        )
        return response_api

    async def answer_pre_checkout_query(self, pre_checkout_query_id: str, ok: bool, *, error_message: Optional[str] = None) -> bool:
        """Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an [Update](https://core.telegram.org/bots/api/#update) with the field *pre_checkout_query*. Use this method to respond to such pre-checkout queries. On success, *True* is returned. **Note:** The Bot API must receive an answer within 10 seconds after the pre-checkout query was sent.

        Args:
            pre_checkout_query_id (str): Unique identifier for the query to be answered
            ok (bool): Specify *True* if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use *False* if there are any problems.
            error_message (str): Required if *ok* is *False*. Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. 'Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!'). Telegram will display this message to the user.
        """
        response_api: bool = await self.exec_request(
            "answerPreCheckoutQuery",
            json={"pre_checkout_query_id": pre_checkout_query_id,
                  "ok": ok,
                  "error_message": error_message},
            return_type=bool  # type: ignore

        )
        return response_api

    async def get_star_transactions(self, *, offset: Optional[int] = None, limit: Optional[int] = 100) -> objects.StarTransactions:
        """Returns the bot's Telegram Star transactions in chronological order. On success, returns a [StarTransactions](https://core.telegram.org/bots/api/#startransactions) object.

        Args:
            offset (int): Number of transactions to skip in the response
            limit (int): The maximum number of transactions to be retrieved. Values between 1-100 are accepted. Defaults to 100.
        """
        response_api: objects.StarTransactions = await self.exec_request(
            "getStarTransactions",
            json={"offset": offset,
                  "limit": limit},
            return_type=objects.StarTransactions  # type: ignore

        )
        return response_api

    async def refund_star_payment(self, user_id: int, telegram_payment_charge_id: str) -> bool:
        """Refunds a successful payment in [Telegram Stars](https://t.me/BotNews/90). Returns *True* on success.

        Args:
            user_id (int): Identifier of the user whose payment will be refunded
            telegram_payment_charge_id (str): Telegram payment identifier
        """
        response_api: bool = await self.exec_request(
            "refundStarPayment",
            json={"user_id": user_id,
                  "telegram_payment_charge_id": telegram_payment_charge_id},
            return_type=bool  # type: ignore

        )
        return response_api

    async def edit_user_star_subscription(self, user_id: int, telegram_payment_charge_id: str, is_canceled: bool) -> bool:
        """Allows the bot to cancel or re-enable extension of a subscription paid in Telegram Stars. Returns *True* on success.

        Args:
            user_id (int): Identifier of the user whose subscription will be edited
            telegram_payment_charge_id (str): Telegram payment identifier for the subscription
            is_canceled (bool): Pass *True* to cancel extension of the user subscription; the subscription must be active up to the end of the current subscription period. Pass *False* to allow the user to re-enable a subscription that was previously canceled by the bot.
        """
        response_api: bool = await self.exec_request(
            "editUserStarSubscription",
            json={"user_id": user_id,
                  "telegram_payment_charge_id": telegram_payment_charge_id,
                  "is_canceled": is_canceled},
            return_type=bool  # type: ignore

        )
        return response_api

    async def set_passport_data_errors(self, user_id: int, errors: List[objects.PassportElementError]) -> bool:
        """Informs a user that some of the Telegram Passport elements they provided contains errors. The user will not be able to re-submit their Passport to you until the errors are fixed (the contents of the field for which you returned the error must change). Returns *True* on success.

Use this if the data submitted by the user doesn't satisfy the standards your service requires for any reason. For example, if a birthday date seems invalid, a submitted document is blurry, a scan shows evidence of tampering, etc. Supply some details in the error message to make sure the user knows how to correct the issues.

        Args:
            user_id (int): User identifier
            errors (List["PassportElementError"]): A JSON-serialized array describing the errors
        """
        response_api: bool = await self.exec_request(
            "setPassportDataErrors",
            json={"user_id": user_id,
                  "errors": errors},
            return_type=bool  # type: ignore

        )
        return response_api

    async def send_game(self, chat_id: int, game_short_name: str, *, business_connection_id: Optional[str] = None, message_thread_id: Optional[int] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None, allow_paid_broadcast: Optional[bool] = None, message_effect_id: Optional[str] = None, reply_parameters: Optional[objects.ReplyParameters] = None, reply_markup: Optional[objects.InlineKeyboardMarkup] = None) -> objects.Message:
        """Use this method to send a game. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.

        Args:
            business_connection_id (str): Unique identifier of the business connection on behalf of which the message will be sent
            chat_id (int): Unique identifier for the target chat
            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
            game_short_name (str): Short name of the game, serves as the unique identifier for the game. Set up your games via [@BotFather](https://t.me/botfather).
            disable_notification (bool): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
            protect_content (bool): Protects the contents of the sent message from forwarding and saving
            allow_paid_broadcast (bool): Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance
            message_effect_id (str): Unique identifier of the message effect to be added to the message; for private chats only
            reply_parameters ("ReplyParameters"): Description of the message to reply to
            reply_markup ("InlineKeyboardMarkup"): A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards). If empty, one 'Play game_title' button will be shown. If not empty, the first button must launch the game.
        """
        response_api: objects.Message = await self.exec_request(
            "sendGame",
            json={"business_connection_id": business_connection_id,
                  "chat_id": chat_id,
                  "message_thread_id": message_thread_id,
                  "game_short_name": game_short_name,
                  "disable_notification": disable_notification,
                  "protect_content": protect_content,
                  "allow_paid_broadcast": allow_paid_broadcast,
                  "message_effect_id": message_effect_id,
                  "reply_parameters": reply_parameters,
                  "reply_markup": reply_markup},
            return_type=objects.Message  # type: ignore

        )
        return response_api

    async def set_game_score(self, user_id: int, score: int, *, force: Optional[bool] = None, disable_edit_message: Optional[bool] = None, chat_id: Optional[int] = None, message_id: Optional[int] = None, inline_message_id: Optional[str] = None) -> Union[objects.Message, bool]:
        """Use this method to set the score of the specified user in a game message. On success, if the message is not an inline message, the [Message](https://core.telegram.org/bots/api/#message) is returned, otherwise *True* is returned. Returns an error, if the new score is not greater than the user's current score in the chat and *force* is *False*.

        Args:
            user_id (int): User identifier
            score (int): New score, must be non-negative
            force (bool): Pass *True* if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters
            disable_edit_message (bool): Pass *True* if the game message should not be automatically edited to include the current scoreboard
            chat_id (int): Required if *inline_message_id* is not specified. Unique identifier for the target chat
            message_id (int): Required if *inline_message_id* is not specified. Identifier of the sent message
            inline_message_id (str): Required if *chat_id* and *message_id* are not specified. Identifier of the inline message
        """
        response_api: Union[objects.Message, bool] = await self.exec_request(
            "setGameScore",
            json={"user_id": user_id,
                  "score": score,
                  "force": force,
                  "disable_edit_message": disable_edit_message,
                  "chat_id": chat_id,
                  "message_id": message_id,
                  "inline_message_id": inline_message_id},
            return_type=Union[objects.Message, bool]  # type: ignore

        )
        return response_api

    async def get_game_high_scores(self, user_id: int, *, chat_id: Optional[int] = None, message_id: Optional[int] = None, inline_message_id: Optional[str] = None) -> List[objects.GameHighScore]:
        """Use this method to get data for high score tables. Will return the score of the specified user and several of their neighbors in a game. Returns an Array of [GameHighScore](https://core.telegram.org/bots/api/#gamehighscore) objects.

This method will currently return scores for the target user, plus two of their closest neighbors on each side. Will also return the top three users if the user and their neighbors are not among them. Please note that this behavior is subject to change.

        Args:
            user_id (int): Target user id
            chat_id (int): Required if *inline_message_id* is not specified. Unique identifier for the target chat
            message_id (int): Required if *inline_message_id* is not specified. Identifier of the sent message
            inline_message_id (str): Required if *chat_id* and *message_id* are not specified. Identifier of the inline message
        """
        response_api: List[objects.GameHighScore] = await self.exec_request(
            "getGameHighScores",
            json={"user_id": user_id,
                  "chat_id": chat_id,
                  "message_id": message_id,
                  "inline_message_id": inline_message_id},
            return_type=List[objects.GameHighScore]  # type: ignore

        )
        return response_api
