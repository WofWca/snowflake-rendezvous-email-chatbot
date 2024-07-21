async function initConnection() {
  const peerConnection = new RTCPeerConnection({
    iceServers: [{ urls: "stun:stun.l.google.com:19302" }],
  });

  peerConnection.createDataChannel("test");

  // const initialOffer = await peerConnection.createOffer();
  await peerConnection.setLocalDescription(await peerConnection.createOffer());
  const webrtcOfferP = new Promise((r) => {
    // Wait for ICE gathering to work for some time.
    setTimeout(() => {
      r(peerConnection.localDescription);
    }, 2000);
  });

  const clientVersion = "1.0";
  const snowflakeClientOffer =
    clientVersion +
    "\n" +
    JSON.stringify({
      offer: JSON.stringify(await webrtcOfferP),
      // Let's not actually test NAT type for this simple example
      nat: "unknown",
      // The default Snowflake bridge.
      fingerprint: "2B280B23E1107BB62ABFC40DDCC8824814F80A72",
    });

  /**
   * @param {string} snowflakeProxyAnswer
   * @param {(newConnectionState: string) => void} onconnectionstatechange
   */
  const connectToProxy = (snowflakeProxyAnswer, onconnectionstatechange) => {
    const webrtcAnswer = JSON.parse(JSON.parse(snowflakeProxyAnswer).answer);
    peerConnection.setRemoteDescription(webrtcAnswer);

    onconnectionstatechange(peerConnection.connectionState);
    peerConnection.onconnectionstatechange = (_ev) => {
      onconnectionstatechange(peerConnection.connectionState);
    };
  };

  return {
    snowflakeClientOffer,
    connectToProxy,
  };
}
