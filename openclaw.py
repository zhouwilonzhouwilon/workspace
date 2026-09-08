import lark_oapi as lark

## P2ImMessageReceiveV1 为接收消息 v2.0；CustomizedEvent 内的 message 为接收消息 v1.0。

def do_p2_im_message_receive_v1(data: lark.im.v1.P2ImMessageReceiveV1) -> None:
    print(f'[ do_p2_im_message_receive_v1 access ], data: {lark.JSON.marshal(data, indent=4)}')
def do_message_event(data: lark.CustomizedEvent) -> None:
    print(f'[ do_customized_event access ], type: message, data: {lark.JSON.marshal(data, indent=4)}')
event_handler = lark.EventDispatcherHandler.builder("", "") \
    .register_p2_im_message_receive_v1(do_p2_im_message_receive_v1) \
    .register_p1_customized_event("out_approval", do_message_event) \
    .build()
def main():
    cli = lark.ws.Client("cli_a93f3c9bd8b8dbcd", "oK2B6MhGBFDjzO9DIB05og2HSTHU606Q",
                         event_handler=event_handler,
                         log_level=lark.LogLevel.DEBUG)
    cli.start()
if __name__ == "__main__":
    main()


# from lark_oapi import Config, Client
# APP_ID="cli_a93f3c9bd8b8dbcd"
# APP_SECRET = "YoK2B6MhGBFDjzO9DIB05og2HSTHU606Q"

# # 如果你是「企业内部应用」（90%的场景）
# config = Config.new_internal_app_config(APP_ID.strip(), APP_SECRET.strip())
# # 如果你是「第三方应用」（需绑定应用商店）
# # config = Config.new_app_config(APP_ID.strip(), APP_SECRET.strip())

# client = Client(config)