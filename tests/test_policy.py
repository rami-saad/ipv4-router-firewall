from policy import allow_packet

def test_block_external_icmp_internal():
    assert allow_packet("1.2.3.4","10.0.1.5","icmp") is False

def test_allow_external_tcp_internal():
    assert allow_packet("1.2.3.4","10.0.1.5","tcp") is True
