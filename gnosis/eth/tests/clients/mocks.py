# noqa

sourcify_safe_metadata = {
    "compiler": {"version": "0.5.17+commit.d19bba13"},
    "language": "Solidity",
    "output": {
        "abi": [
            {
                "inputs": [],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "constructor",
            },
            {
                "anonymous": False,
                "inputs": [
                    {
                        "indexed": False,
                        "internalType": "address",
                        "name": "owner",
                        "type": "address",
                    }
                ],
                "name": "AddedOwner",
                "type": "event",
            },
            {
                "anonymous": False,
                "inputs": [
                    {
                        "indexed": True,
                        "internalType": "bytes32",
                        "name": "approvedHash",
                        "type": "bytes32",
                    },
                    {
                        "indexed": True,
                        "internalType": "address",
                        "name": "owner",
                        "type": "address",
                    },
                ],
                "name": "ApproveHash",
                "type": "event",
            },
            {
                "anonymous": False,
                "inputs": [
                    {
                        "indexed": False,
                        "internalType": "address",
                        "name": "masterCopy",
                        "type": "address",
                    }
                ],
                "name": "ChangedMasterCopy",
                "type": "event",
            },
            {
                "anonymous": False,
                "inputs": [
                    {
                        "indexed": False,
                        "internalType": "uint256",
                        "name": "threshold",
                        "type": "uint256",
                    }
                ],
                "name": "ChangedThreshold",
                "type": "event",
            },
            {
                "anonymous": False,
                "inputs": [
                    {
                        "indexed": False,
                        "internalType": "contract Module",
                        "name": "module",
                        "type": "address",
                    }
                ],
                "name": "DisabledModule",
                "type": "event",
            },
            {
                "anonymous": False,
                "inputs": [
                    {
                        "indexed": False,
                        "internalType": "contract Module",
                        "name": "module",
                        "type": "address",
                    }
                ],
                "name": "EnabledModule",
                "type": "event",
            },
            {
                "anonymous": False,
                "inputs": [
                    {
                        "indexed": False,
                        "internalType": "bytes32",
                        "name": "txHash",
                        "type": "bytes32",
                    },
                    {
                        "indexed": False,
                        "internalType": "uint256",
                        "name": "payment",
                        "type": "uint256",
                    },
                ],
                "name": "ExecutionFailure",
                "type": "event",
            },
            {
                "anonymous": False,
                "inputs": [
                    {
                        "indexed": True,
                        "internalType": "address",
                        "name": "module",
                        "type": "address",
                    }
                ],
                "name": "ExecutionFromModuleFailure",
                "type": "event",
            },
            {
                "anonymous": False,
                "inputs": [
                    {
                        "indexed": True,
                        "internalType": "address",
                        "name": "module",
                        "type": "address",
                    }
                ],
                "name": "ExecutionFromModuleSuccess",
                "type": "event",
            },
            {
                "anonymous": False,
                "inputs": [
                    {
                        "indexed": False,
                        "internalType": "bytes32",
                        "name": "txHash",
                        "type": "bytes32",
                    },
                    {
                        "indexed": False,
                        "internalType": "uint256",
                        "name": "payment",
                        "type": "uint256",
                    },
                ],
                "name": "ExecutionSuccess",
                "type": "event",
            },
            {
                "anonymous": False,
                "inputs": [
                    {
                        "indexed": False,
                        "internalType": "address",
                        "name": "owner",
                        "type": "address",
                    }
                ],
                "name": "RemovedOwner",
                "type": "event",
            },
            {
                "anonymous": False,
                "inputs": [
                    {
                        "indexed": True,
                        "internalType": "bytes32",
                        "name": "msgHash",
                        "type": "bytes32",
                    }
                ],
                "name": "SignMsg",
                "type": "event",
            },
            {"payable": True, "stateMutability": "payable", "type": "fallback"},
            {
                "constant": True,
                "inputs": [],
                "name": "NAME",
                "outputs": [{"internalType": "string", "name": "", "type": "string"}],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            },
            {
                "constant": True,
                "inputs": [],
                "name": "VERSION",
                "outputs": [{"internalType": "string", "name": "", "type": "string"}],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            },
            {
                "constant": False,
                "inputs": [
                    {"internalType": "address", "name": "owner", "type": "address"},
                    {
                        "internalType": "uint256",
                        "name": "_threshold",
                        "type": "uint256",
                    },
                ],
                "name": "addOwnerWithThreshold",
                "outputs": [],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function",
            },
            {
                "constant": False,
                "inputs": [
                    {
                        "internalType": "bytes32",
                        "name": "hashToApprove",
                        "type": "bytes32",
                    }
                ],
                "name": "approveHash",
                "outputs": [],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function",
            },
            {
                "constant": True,
                "inputs": [
                    {"internalType": "address", "name": "", "type": "address"},
                    {"internalType": "bytes32", "name": "", "type": "bytes32"},
                ],
                "name": "approvedHashes",
                "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            },
            {
                "constant": False,
                "inputs": [
                    {
                        "internalType": "address",
                        "name": "_masterCopy",
                        "type": "address",
                    }
                ],
                "name": "changeMasterCopy",
                "outputs": [],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function",
            },
            {
                "constant": False,
                "inputs": [
                    {"internalType": "uint256", "name": "_threshold", "type": "uint256"}
                ],
                "name": "changeThreshold",
                "outputs": [],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function",
            },
            {
                "constant": False,
                "inputs": [
                    {
                        "internalType": "contract Module",
                        "name": "prevModule",
                        "type": "address",
                    },
                    {
                        "internalType": "contract Module",
                        "name": "module",
                        "type": "address",
                    },
                ],
                "name": "disableModule",
                "outputs": [],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function",
            },
            {
                "constant": True,
                "inputs": [],
                "name": "domainSeparator",
                "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            },
            {
                "constant": False,
                "inputs": [
                    {
                        "internalType": "contract Module",
                        "name": "module",
                        "type": "address",
                    }
                ],
                "name": "enableModule",
                "outputs": [],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function",
            },
            {
                "constant": True,
                "inputs": [
                    {"internalType": "address", "name": "to", "type": "address"},
                    {"internalType": "uint256", "name": "value", "type": "uint256"},
                    {"internalType": "bytes", "name": "data", "type": "bytes"},
                    {
                        "internalType": "enum Enum.Operation",
                        "name": "operation",
                        "type": "uint8",
                    },
                    {"internalType": "uint256", "name": "safeTxGas", "type": "uint256"},
                    {"internalType": "uint256", "name": "baseGas", "type": "uint256"},
                    {"internalType": "uint256", "name": "gasPrice", "type": "uint256"},
                    {"internalType": "address", "name": "gasToken", "type": "address"},
                    {
                        "internalType": "address",
                        "name": "refundReceiver",
                        "type": "address",
                    },
                    {"internalType": "uint256", "name": "_nonce", "type": "uint256"},
                ],
                "name": "encodeTransactionData",
                "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            },
            {
                "constant": False,
                "inputs": [
                    {"internalType": "address", "name": "to", "type": "address"},
                    {"internalType": "uint256", "name": "value", "type": "uint256"},
                    {"internalType": "bytes", "name": "data", "type": "bytes"},
                    {
                        "internalType": "enum Enum.Operation",
                        "name": "operation",
                        "type": "uint8",
                    },
                    {"internalType": "uint256", "name": "safeTxGas", "type": "uint256"},
                    {"internalType": "uint256", "name": "baseGas", "type": "uint256"},
                    {"internalType": "uint256", "name": "gasPrice", "type": "uint256"},
                    {"internalType": "address", "name": "gasToken", "type": "address"},
                    {
                        "internalType": "address payable",
                        "name": "refundReceiver",
                        "type": "address",
                    },
                    {"internalType": "bytes", "name": "signatures", "type": "bytes"},
                ],
                "name": "execTransaction",
                "outputs": [
                    {"internalType": "bool", "name": "success", "type": "bool"}
                ],
                "payable": True,
                "stateMutability": "payable",
                "type": "function",
            },
            {
                "constant": False,
                "inputs": [
                    {"internalType": "address", "name": "to", "type": "address"},
                    {"internalType": "uint256", "name": "value", "type": "uint256"},
                    {"internalType": "bytes", "name": "data", "type": "bytes"},
                    {
                        "internalType": "enum Enum.Operation",
                        "name": "operation",
                        "type": "uint8",
                    },
                ],
                "name": "execTransactionFromModule",
                "outputs": [
                    {"internalType": "bool", "name": "success", "type": "bool"}
                ],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function",
            },
            {
                "constant": False,
                "inputs": [
                    {"internalType": "address", "name": "to", "type": "address"},
                    {"internalType": "uint256", "name": "value", "type": "uint256"},
                    {"internalType": "bytes", "name": "data", "type": "bytes"},
                    {
                        "internalType": "enum Enum.Operation",
                        "name": "operation",
                        "type": "uint8",
                    },
                ],
                "name": "execTransactionFromModuleReturnData",
                "outputs": [
                    {"internalType": "bool", "name": "success", "type": "bool"},
                    {"internalType": "bytes", "name": "returnData", "type": "bytes"},
                ],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function",
            },
            {
                "constant": True,
                "inputs": [
                    {"internalType": "bytes", "name": "message", "type": "bytes"}
                ],
                "name": "getMessageHash",
                "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            },
            {
                "constant": True,
                "inputs": [],
                "name": "getModules",
                "outputs": [
                    {"internalType": "address[]", "name": "", "type": "address[]"}
                ],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            },
            {
                "constant": True,
                "inputs": [
                    {"internalType": "address", "name": "start", "type": "address"},
                    {"internalType": "uint256", "name": "pageSize", "type": "uint256"},
                ],
                "name": "getModulesPaginated",
                "outputs": [
                    {"internalType": "address[]", "name": "array", "type": "address[]"},
                    {"internalType": "address", "name": "next", "type": "address"},
                ],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            },
            {
                "constant": True,
                "inputs": [],
                "name": "getOwners",
                "outputs": [
                    {"internalType": "address[]", "name": "", "type": "address[]"}
                ],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            },
            {
                "constant": True,
                "inputs": [],
                "name": "getThreshold",
                "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            },
            {
                "constant": True,
                "inputs": [
                    {"internalType": "address", "name": "to", "type": "address"},
                    {"internalType": "uint256", "name": "value", "type": "uint256"},
                    {"internalType": "bytes", "name": "data", "type": "bytes"},
                    {
                        "internalType": "enum Enum.Operation",
                        "name": "operation",
                        "type": "uint8",
                    },
                    {"internalType": "uint256", "name": "safeTxGas", "type": "uint256"},
                    {"internalType": "uint256", "name": "baseGas", "type": "uint256"},
                    {"internalType": "uint256", "name": "gasPrice", "type": "uint256"},
                    {"internalType": "address", "name": "gasToken", "type": "address"},
                    {
                        "internalType": "address",
                        "name": "refundReceiver",
                        "type": "address",
                    },
                    {"internalType": "uint256", "name": "_nonce", "type": "uint256"},
                ],
                "name": "getTransactionHash",
                "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            },
            {
                "constant": True,
                "inputs": [
                    {
                        "internalType": "contract Module",
                        "name": "module",
                        "type": "address",
                    }
                ],
                "name": "isModuleEnabled",
                "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            },
            {
                "constant": True,
                "inputs": [
                    {"internalType": "address", "name": "owner", "type": "address"}
                ],
                "name": "isOwner",
                "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            },
            {
                "constant": False,
                "inputs": [
                    {"internalType": "bytes", "name": "_data", "type": "bytes"},
                    {"internalType": "bytes", "name": "_signature", "type": "bytes"},
                ],
                "name": "isValidSignature",
                "outputs": [{"internalType": "bytes4", "name": "", "type": "bytes4"}],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function",
            },
            {
                "constant": True,
                "inputs": [],
                "name": "nonce",
                "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            },
            {
                "constant": False,
                "inputs": [
                    {"internalType": "address", "name": "prevOwner", "type": "address"},
                    {"internalType": "address", "name": "owner", "type": "address"},
                    {
                        "internalType": "uint256",
                        "name": "_threshold",
                        "type": "uint256",
                    },
                ],
                "name": "removeOwner",
                "outputs": [],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function",
            },
            {
                "constant": False,
                "inputs": [
                    {"internalType": "address", "name": "to", "type": "address"},
                    {"internalType": "uint256", "name": "value", "type": "uint256"},
                    {"internalType": "bytes", "name": "data", "type": "bytes"},
                    {
                        "internalType": "enum Enum.Operation",
                        "name": "operation",
                        "type": "uint8",
                    },
                ],
                "name": "requiredTxGas",
                "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function",
            },
            {
                "constant": False,
                "inputs": [
                    {"internalType": "address", "name": "handler", "type": "address"}
                ],
                "name": "setFallbackHandler",
                "outputs": [],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function",
            },
            {
                "constant": False,
                "inputs": [
                    {
                        "internalType": "address[]",
                        "name": "_owners",
                        "type": "address[]",
                    },
                    {
                        "internalType": "uint256",
                        "name": "_threshold",
                        "type": "uint256",
                    },
                    {"internalType": "address", "name": "to", "type": "address"},
                    {"internalType": "bytes", "name": "data", "type": "bytes"},
                    {
                        "internalType": "address",
                        "name": "fallbackHandler",
                        "type": "address",
                    },
                    {
                        "internalType": "address",
                        "name": "paymentToken",
                        "type": "address",
                    },
                    {"internalType": "uint256", "name": "payment", "type": "uint256"},
                    {
                        "internalType": "address payable",
                        "name": "paymentReceiver",
                        "type": "address",
                    },
                ],
                "name": "setup",
                "outputs": [],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function",
            },
            {
                "constant": False,
                "inputs": [{"internalType": "bytes", "name": "_data", "type": "bytes"}],
                "name": "signMessage",
                "outputs": [],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function",
            },
            {
                "constant": True,
                "inputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
                "name": "signedMessages",
                "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            },
            {
                "constant": False,
                "inputs": [
                    {"internalType": "address", "name": "prevOwner", "type": "address"},
                    {"internalType": "address", "name": "oldOwner", "type": "address"},
                    {"internalType": "address", "name": "newOwner", "type": "address"},
                ],
                "name": "swapOwner",
                "outputs": [],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function",
            },
        ],
        "devdoc": {
            "author": "Stefan George - <stefan@gnosis.io>Richard Meissner - <richard@gnosis.io>Ricardo Guilherme Schmidt - (Status Research & Development GmbH) - Gas Token Payment",
            "methods": {
                "addOwnerWithThreshold(address,uint256)": {
                    "details": "Allows to add a new owner to the Safe and update the threshold at the same time.      This can only be done via a Safe transaction.",
                    "params": {
                        "_threshold": "New threshold.",
                        "owner": "New owner address.",
                    },
                },
                "approveHash(bytes32)": {
                    "details": "Marks a hash as approved. This can be used to validate a hash that is used by a signature.",
                    "params": {
                        "hashToApprove": "The hash that should be marked as approved for signatures that are verified by this contract."
                    },
                },
                "changeMasterCopy(address)": {
                    "details": "Allows to upgrade the contract. This can only be done via a Safe transaction.",
                    "params": {"_masterCopy": "New contract address."},
                },
                "changeThreshold(uint256)": {
                    "details": "Allows to update the number of required confirmations by Safe owners.      This can only be done via a Safe transaction.",
                    "params": {"_threshold": "New threshold."},
                },
                "disableModule(address,address)": {
                    "details": "Allows to remove a module from the whitelist.      This can only be done via a Safe transaction.",
                    "params": {
                        "module": "Module to be removed.",
                        "prevModule": "Module that pointed to the module to be removed in the linked list",
                    },
                },
                "enableModule(address)": {
                    "details": "Allows to add a module to the whitelist.      This can only be done via a Safe transaction.",
                    "params": {"module": "Module to be whitelisted."},
                },
                "encodeTransactionData(address,uint256,bytes,uint8,uint256,uint256,uint256,address,address,uint256)": {
                    "details": "Returns the bytes that are hashed to be signed by owners.",
                    "params": {
                        "_nonce": "Transaction nonce.",
                        "baseGas": "Gas costs for data used to trigger the safe transaction.",
                        "data": "Data payload.",
                        "gasPrice": "Maximum gas price that should be used for this transaction.",
                        "gasToken": "Token address (or 0 if ETH) that is used for the payment.",
                        "operation": "Operation type.",
                        "refundReceiver": "Address of receiver of gas payment (or 0 if tx.origin).",
                        "safeTxGas": "Fas that should be used for the safe transaction.",
                        "to": "Destination address.",
                        "value": "Ether value.",
                    },
                    "return": "Transaction hash bytes.",
                },
                "execTransaction(address,uint256,bytes,uint8,uint256,uint256,uint256,address,address,bytes)": {
                    "details": "Allows to execute a Safe transaction confirmed by required number of owners and then pays the account that submitted the transaction.      Note: The fees are always transfered, even if the user transaction fails.",
                    "params": {
                        "baseGas": "Gas costs for that are indipendent of the transaction execution(e.g. base transaction fee, signature check, payment of the refund)",
                        "data": "Data payload of Safe transaction.",
                        "gasPrice": "Gas price that should be used for the payment calculation.",
                        "gasToken": "Token address (or 0 if ETH) that is used for the payment.",
                        "operation": "Operation type of Safe transaction.",
                        "refundReceiver": "Address of receiver of gas payment (or 0 if tx.origin).",
                        "safeTxGas": "Gas that should be used for the Safe transaction.",
                        "signatures": "Packed signature data ({bytes32 r}{bytes32 s}{uint8 v})",
                        "to": "Destination address of Safe transaction.",
                        "value": "Ether value of Safe transaction.",
                    },
                },
                "execTransactionFromModule(address,uint256,bytes,uint8)": {
                    "details": "Allows a Module to execute a Safe transaction without any further confirmations.",
                    "params": {
                        "data": "Data payload of module transaction.",
                        "operation": "Operation type of module transaction.",
                        "to": "Destination address of module transaction.",
                        "value": "Ether value of module transaction.",
                    },
                },
                "execTransactionFromModuleReturnData(address,uint256,bytes,uint8)": {
                    "details": "Allows a Module to execute a Safe transaction without any further confirmations and return data",
                    "params": {
                        "data": "Data payload of module transaction.",
                        "operation": "Operation type of module transaction.",
                        "to": "Destination address of module transaction.",
                        "value": "Ether value of module transaction.",
                    },
                },
                "getMessageHash(bytes)": {
                    "details": "Returns hash of a message that can be signed by owners.",
                    "params": {"message": "Message that should be hashed"},
                    "return": "Message hash.",
                },
                "getModules()": {
                    "details": "Returns array of first 10 modules.",
                    "return": "Array of modules.",
                },
                "getModulesPaginated(address,uint256)": {
                    "details": "Returns array of modules.",
                    "params": {
                        "pageSize": "Maximum number of modules that should be returned.",
                        "start": "Start of the page.",
                    },
                    "return": "Array of modules.",
                },
                "getOwners()": {
                    "details": "Returns array of owners.",
                    "return": "Array of Safe owners.",
                },
                "getTransactionHash(address,uint256,bytes,uint8,uint256,uint256,uint256,address,address,uint256)": {
                    "details": "Returns hash to be signed by owners.",
                    "params": {
                        "_nonce": "Transaction nonce.",
                        "baseGas": "Gas costs for data used to trigger the safe transaction.",
                        "data": "Data payload.",
                        "gasPrice": "Maximum gas price that should be used for this transaction.",
                        "gasToken": "Token address (or 0 if ETH) that is used for the payment.",
                        "operation": "Operation type.",
                        "refundReceiver": "Address of receiver of gas payment (or 0 if tx.origin).",
                        "safeTxGas": "Fas that should be used for the safe transaction.",
                        "to": "Destination address.",
                        "value": "Ether value.",
                    },
                    "return": "Transaction hash.",
                },
                "isModuleEnabled(address)": {
                    "details": "Returns if an module is enabled",
                    "return": "True if the module is enabled",
                },
                "isValidSignature(bytes,bytes)": {
                    "details": "Should return whether the signature provided is valid for the provided data.      The save does not implement the interface since `checkSignatures` is not a view method.      The method will not perform any state changes (see parameters of `checkSignatures`)",
                    "params": {
                        "_data": "Arbitrary length data signed on the behalf of address(this)",
                        "_signature": "Signature byte array associated with _data",
                    },
                    "return": "a bool upon valid or invalid signature with corresponding _data",
                },
                "removeOwner(address,address,uint256)": {
                    "details": "Allows to remove an owner from the Safe and update the threshold at the same time.      This can only be done via a Safe transaction.",
                    "params": {
                        "_threshold": "New threshold.",
                        "owner": "Owner address to be removed.",
                        "prevOwner": "Owner that pointed to the owner to be removed in the linked list",
                    },
                },
                "requiredTxGas(address,uint256,bytes,uint8)": {
                    "details": "Allows to estimate a Safe transaction.      This method is only meant for estimation purpose, therefore two different protection mechanism against execution in a transaction have been made:      1.) The method can only be called from the safe itself      2.) The response is returned with a revert      When estimating set `from` to the address of the safe.      Since the `estimateGas` function includes refunds, call this method to get an estimated of the costs that are deducted from the safe with `execTransaction`",
                    "params": {
                        "data": "Data payload of Safe transaction.",
                        "operation": "Operation type of Safe transaction.",
                        "to": "Destination address of Safe transaction.",
                        "value": "Ether value of Safe transaction.",
                    },
                    "return": "Estimate without refunds and overhead fees (base transaction and payload data gas costs).",
                },
                "setFallbackHandler(address)": {
                    "details": "Allows to add a contract to handle fallback calls.      Only fallback calls without value and with data will be forwarded.      This can only be done via a Safe transaction.",
                    "params": {"handler": "contract to handle fallbacks calls."},
                },
                "setup(address[],uint256,address,bytes,address,address,uint256,address)": {
                    "details": "Setup function sets initial storage of contract.",
                    "params": {
                        "_owners": "List of Safe owners.",
                        "_threshold": "Number of required confirmations for a Safe transaction.",
                        "data": "Data payload for optional delegate call.",
                        "fallbackHandler": "Handler for fallback calls to this contract",
                        "payment": "Value that should be paid",
                        "paymentReceiver": "Adddress that should receive the payment (or 0 if tx.origin)",
                        "paymentToken": "Token that should be used for the payment (0 is ETH)",
                        "to": "Contract address for optional delegate call.",
                    },
                },
                "signMessage(bytes)": {
                    "details": "Marks a message as signed, so that it can be used with EIP-1271",
                    "params": {
                        "_data": "Arbitrary length data that should be marked as signed on the behalf of address(this)"
                    },
                },
                "swapOwner(address,address,address)": {
                    "details": "Allows to swap/replace an owner from the Safe with another address.      This can only be done via a Safe transaction.",
                    "params": {
                        "newOwner": "New owner address.",
                        "oldOwner": "Owner address to be replaced.",
                        "prevOwner": "Owner that pointed to the owner to be replaced in the linked list",
                    },
                },
            },
            "title": "Gnosis Safe - A multisignature wallet with support for confirmations using signed messages based on ERC191.",
        },
        "userdoc": {
            "methods": {
                "addOwnerWithThreshold(address,uint256)": {
                    "notice": "Adds the owner `owner` to the Safe and updates the threshold to `_threshold`."
                },
                "changeThreshold(uint256)": {
                    "notice": "Changes the threshold of the Safe to `_threshold`."
                },
                "disableModule(address,address)": {
                    "notice": "Disables the module `module` for the Safe."
                },
                "enableModule(address)": {
                    "notice": "Enables the module `module` for the Safe."
                },
                "isValidSignature(bytes,bytes)": {
                    "notice": "Implementation of ISignatureValidator (see `interfaces/ISignatureValidator.sol`)"
                },
                "removeOwner(address,address,uint256)": {
                    "notice": "Removes the owner `owner` from the Safe and updates the threshold to `_threshold`."
                },
                "signMessage(bytes)": {
                    "notice": "Marks a message (`_data`) as signed."
                },
                "swapOwner(address,address,address)": {
                    "notice": "Replaces the owner `oldOwner` in the Safe with `newOwner`."
                },
            }
        },
    },
    "settings": {
        "compilationTarget": {"/gnosis-safe/contracts/GnosisSafe.sol": "GnosisSafe"},
        "evmVersion": "petersburg",
        "libraries": {},
        "optimizer": {"enabled": False, "runs": 200},
        "remappings": [],
    },
    "sources": {
        "/gnosis-safe/contracts/GnosisSafe.sol": {
            "keccak256": "0x8c12335842166d5a6a6d320afe4ccbef706524ff38a2d0946ef92f4e33c557ae",
            "urls": [
                "bzz-raw://8bdb6cc4fdaf3c87426410ebd6c8a5d4042ac9a9340fcf0bca8b60a39b53f6e4",
                "dweb:/ipfs/QmZi8d73z5Rgtwx4FJ658cTzSgfmSwYHR3ajwmzfo1HQNf",
            ],
        },
        "/gnosis-safe/contracts/base/Executor.sol": {
            "keccak256": "0xd2835623a200b6f14979751aff14e48362b5db0d86fff17dfb6a982790ff6c67",
            "urls": [
                "bzz-raw://df85c3b4dc546ffd8790a155bf6190b55168a69f469624a9134f1e7a9e079880",
                "dweb:/ipfs/QmXozPPHk7KAyoihdx4FEn4dEaR2x9yDJthQcZPR3Knxpv",
            ],
        },
        "/gnosis-safe/contracts/base/FallbackManager.sol": {
            "keccak256": "0x18baeb026940c7a06ee4aceebed0118b920468777e2f08a45d39c0983ee57523",
            "urls": [
                "bzz-raw://75ec51dbc17c5e5c6701ed6809ea6c0d8bbd8dfdca944ed00d64d6f96fde98f0",
                "dweb:/ipfs/QmTbJz9p6oro7MCZKHBBBeoowQNYv7raQnoC5bfWxoQ4vR",
            ],
        },
        "/gnosis-safe/contracts/base/Module.sol": {
            "keccak256": "0x0d168bb2c28fe04185e992692705925d700ecc32692e1a1f997478c55722b9ad",
            "urls": [
                "bzz-raw://72b39ab237628e99e68b89269a99efbf7f4c977ce8dcda9e947e74ffffc2bf36",
                "dweb:/ipfs/QmekYYrv5X2wdg2QqaP96qhkxpwTT8nt47CHvuBxzHv9hp",
            ],
        },
        "/gnosis-safe/contracts/base/ModuleManager.sol": {
            "keccak256": "0xb37522d525b7bc868df406e3779ff764f74d74354dc8e86ad4590afb62722117",
            "urls": [
                "bzz-raw://797f422109bdb6517916c41697cf834cafc14ce2bab8140b26847aa27fc95523",
                "dweb:/ipfs/QmNMXB1tBH9tJfmNqteUKdD8RXKXX9jNscz6Y5ijxqzGAL",
            ],
        },
        "/gnosis-safe/contracts/base/OwnerManager.sol": {
            "keccak256": "0x0b4e23b1ba1f82475822f9fd3c7286190219f930f8917e8c5abb7e934a2fa9ef",
            "urls": [
                "bzz-raw://30adee483c783750415a0ebac930e9d97d1da49d90c52ceeb02a65263ab4d1e5",
                "dweb:/ipfs/Qma7RcT3LfzQrdpG2uBMbpx1qQbL2TF91UfANdeGUct2AT",
            ],
        },
        "/gnosis-safe/contracts/common/Enum.sol": {
            "keccak256": "0x7bc6e5afb9436d9f7e376c2cdba51ca1f337e1b31c04cca5769db3a77ed40081",
            "urls": [
                "bzz-raw://88b3a68baaff962b69b040af62698034bf9c99319e4a6dce71abc2c0c88fba91",
                "dweb:/ipfs/QmTefyhXcMALQew96u7YRLQBnye9vapqkKBWxbynWpMHDM",
            ],
        },
        "/gnosis-safe/contracts/common/MasterCopy.sol": {
            "keccak256": "0x1577fad0dc06cb3ac2c7d66816a00d3b70c053a21ab5834ec7aceace9a7803a7",
            "urls": [
                "bzz-raw://7f23c1e11ebb2fbd3b55a4074b4a9f343c0ac02b372cbbe66a90d71a88ce1885",
                "dweb:/ipfs/QmexSrdAm4DqBjGi29yQTxSGKqJ5qC8jy1b5NJH6Zy9Cvh",
            ],
        },
        "/gnosis-safe/contracts/common/SecuredTokenTransfer.sol": {
            "keccak256": "0xefb71775825579db9bab375c4e620deaf266b00a3e8c49ba382551c1dc3b66e9",
            "urls": [
                "bzz-raw://4c57d5ba7c81d72c0e537e68bc957c7429110447dc307f2a4b054594d1068603",
                "dweb:/ipfs/QmeEYz4hKpfpHLU8D1BDutWa1ZBav2idBfhWxtXZtrb8Vp",
            ],
        },
        "/gnosis-safe/contracts/common/SelfAuthorized.sol": {
            "keccak256": "0x4c4f094227fc466846a97fe375c47ecdfcab050c303baeb69b5970d28db717a6",
            "urls": [
                "bzz-raw://42759fe6b2433ea24fd0fbe98a144ef55e464f87861a13aa364db8a6f4a01cf1",
                "dweb:/ipfs/QmTWPnHdfcBbddkMJxvEvoWs3CZoKB5rtz3s8K2ii9z9CG",
            ],
        },
        "/gnosis-safe/contracts/common/SignatureDecoder.sol": {
            "keccak256": "0x9d6196319963155fd0a1dd45e6d4992489da251e18572c2fc62084482edb37a9",
            "urls": [
                "bzz-raw://0298c7d98d2368bc99ae8d28befc8d40250fd7128f45095321d3c9e199fec74b",
                "dweb:/ipfs/QmPK4Q2mSnsEuv5ayyDAzURAksYXmbbALQ2Z5xUcfx1q4K",
            ],
        },
        "/gnosis-safe/contracts/external/GnosisSafeMath.sol": {
            "keccak256": "0xc8d2d226f9cf7d0e1bd8192e7e08c5b33c03413cf045c035b00e6665fc86d5bc",
            "urls": [
                "bzz-raw://f2dc8f2f786e4e674814332f6e839d69dd282707ea0016c8349a86bbf006eb0f",
                "dweb:/ipfs/QmPJhejgQw2hmtCPJa5p9Dq4jbnYr3PrHx6E1T356TyYci",
            ],
        },
        "/gnosis-safe/contracts/interfaces/ISignatureValidator.sol": {
            "keccak256": "0xb75555e8e2bbbe38c55e164dde9761a016b0b4f1b0004b93d7ec2acd873faca4",
            "urls": [
                "bzz-raw://5985325d13e7aedb3036e9f342e740c14bf57b6202b11c2a36f95867f8c9ad5e",
                "dweb:/ipfs/QmTRKm25xk4jsTQHww3JtaU9fNp1BiM6SKoUNp5LrcLyo5",
            ],
        },
    },
    "version": 1,
}


etherscan_source_code_mock = [
    {
        "SourceCode": '{{\r\n  "language": "Solidity",\r\n  "sources": {\r\n    "/gnosis-safe/contracts/GnosisSafe.sol": {\r\n      "content": "pragma solidity >=0.5.0 <0.7.0;\\nimport \\"./base/ModuleManager.sol\\";\\nimport \\"./base/OwnerManager.sol\\";\\nimport \\"./base/FallbackManager.sol\\";\\nimport \\"./common/MasterCopy.sol\\";\\nimport \\"./common/SignatureDecoder.sol\\";\\nimport \\"./common/SecuredTokenTransfer.sol\\";\\nimport \\"./interfaces/ISignatureValidator.sol\\";\\nimport \\"./external/GnosisSafeMath.sol\\";\\n\\n/// @title Gnosis Safe - A multisignature wallet with support for confirmations using signed messages based on ERC191.\\n/// @author Stefan George - <stefan@gnosis.io>\\n/// @author Richard Meissner - <richard@gnosis.io>\\n/// @author Ricardo Guilherme Schmidt - (Status Research & Development GmbH) - Gas Token Payment\\ncontract GnosisSafe\\n    is MasterCopy, ModuleManager, OwnerManager, SignatureDecoder, SecuredTokenTransfer, ISignatureValidatorConstants, FallbackManager {\\n\\n    using GnosisSafeMath for uint256;\\n\\n    string public constant NAME = \\"Gnosis Safe\\";\\n    string public constant VERSION = \\"1.2.0\\";\\n\\n    //keccak256(\\n    //    \\"EIP712Domain(address verifyingContract)\\"\\n    //);\\n    bytes32 private constant DOMAIN_SEPARATOR_TYPEHASH = 0x035aff83d86937d35b32e04f0ddc6ff469290eef2f1b692d8a815c89404d4749;\\n\\n    //keccak256(\\n    //    \\"SafeTx(address to,uint256 value,bytes data,uint8 operation,uint256 safeTxGas,uint256 baseGas,uint256 gasPrice,address gasToken,address refundReceiver,uint256 nonce)\\"\\n    //);\\n    bytes32 private constant SAFE_TX_TYPEHASH = 0xbb8310d486368db6bd6f849402fdd73ad53d316b5a4b2644ad6efe0f941286d8;\\n\\n    //keccak256(\\n    //    \\"SafeMessage(bytes message)\\"\\n    //);\\n    bytes32 private constant SAFE_MSG_TYPEHASH = 0x60b3cbf8b4a223d68d641b3b6ddf9a298e7f33710cf3d3a9d1146b5a6150fbca;\\n\\n    event ApproveHash(\\n        bytes32 indexed approvedHash,\\n        address indexed owner\\n    );\\n    event SignMsg(\\n        bytes32 indexed msgHash\\n    );\\n    event ExecutionFailure(\\n        bytes32 txHash, uint256 payment\\n    );\\n    event ExecutionSuccess(\\n        bytes32 txHash, uint256 payment\\n    );\\n\\n    uint256 public nonce;\\n    bytes32 public domainSeparator;\\n    // Mapping to keep track of all message hashes that have been approve by ALL REQUIRED owners\\n    mapping(bytes32 => uint256) public signedMessages;\\n    // Mapping to keep track of all hashes (message or transaction) that have been approve by ANY owners\\n    mapping(address => mapping(bytes32 => uint256)) public approvedHashes;\\n\\n    // This constructor ensures that this contract can only be used as a master copy for Proxy contracts\\n    constructor() public {\\n        // By setting the threshold it is not possible to call setup anymore,\\n        // so we create a Safe with 0 owners and threshold 1.\\n        // This is an unusable Safe, perfect for the mastercopy\\n        threshold = 1;\\n    }\\n\\n    /// @dev Setup function sets initial storage of contract.\\n    /// @param _owners List of Safe owners.\\n    /// @param _threshold Number of required confirmations for a Safe transaction.\\n    /// @param to Contract address for optional delegate call.\\n    /// @param data Data payload for optional delegate call.\\n    /// @param fallbackHandler Handler for fallback calls to this contract\\n    /// @param paymentToken Token that should be used for the payment (0 is ETH)\\n    /// @param payment Value that should be paid\\n    /// @param paymentReceiver Adddress that should receive the payment (or 0 if tx.origin)\\n    function setup(\\n        address[] calldata _owners,\\n        uint256 _threshold,\\n        address to,\\n        bytes calldata data,\\n        address fallbackHandler,\\n        address paymentToken,\\n        uint256 payment,\\n        address payable paymentReceiver\\n    )\\n        external\\n    {\\n        require(domainSeparator == 0, \\"Domain Separator already set!\\");\\n        domainSeparator = keccak256(abi.encode(DOMAIN_SEPARATOR_TYPEHASH, this));\\n        setupOwners(_owners, _threshold);\\n        if (fallbackHandler != address(0)) internalSetFallbackHandler(fallbackHandler);\\n        // As setupOwners can only be called if the contract has not been initialized we don\'t need a check for setupModules\\n        setupModules(to, data);\\n\\n        if (payment > 0) {\\n            // To avoid running into issues with EIP-170 we reuse the handlePayment function (to avoid adjusting code of that has been verified we do not adjust the method itself)\\n            // baseGas = 0, gasPrice = 1 and gas = payment => amount = (payment + 0) * 1 = payment\\n            handlePayment(payment, 0, 1, paymentToken, paymentReceiver);\\n        }\\n    }\\n\\n    /// @dev Allows to execute a Safe transaction confirmed by required number of owners and then pays the account that submitted the transaction.\\n    ///      Note: The fees are always transfered, even if the user transaction fails.\\n    /// @param to Destination address of Safe transaction.\\n    /// @param value Ether value of Safe transaction.\\n    /// @param data Data payload of Safe transaction.\\n    /// @param operation Operation type of Safe transaction.\\n    /// @param safeTxGas Gas that should be used for the Safe transaction.\\n    /// @param baseGas Gas costs for that are indipendent of the transaction execution(e.g. base transaction fee, signature check, payment of the refund)\\n    /// @param gasPrice Gas price that should be used for the payment calculation.\\n    /// @param gasToken Token address (or 0 if ETH) that is used for the payment.\\n    /// @param refundReceiver Address of receiver of gas payment (or 0 if tx.origin).\\n    /// @param signatures Packed signature data ({bytes32 r}{bytes32 s}{uint8 v})\\n    function execTransaction(\\n        address to,\\n        uint256 value,\\n        bytes calldata data,\\n        Enum.Operation operation,\\n        uint256 safeTxGas,\\n        uint256 baseGas,\\n        uint256 gasPrice,\\n        address gasToken,\\n        address payable refundReceiver,\\n        bytes calldata signatures\\n    )\\n        external\\n        payable\\n        returns (bool success)\\n    {\\n        bytes32 txHash;\\n        // Use scope here to limit variable lifetime and prevent `stack too deep` errors\\n        {\\n            bytes memory txHashData = encodeTransactionData(\\n                to, value, data, operation, // Transaction info\\n                safeTxGas, baseGas, gasPrice, gasToken, refundReceiver, // Payment info\\n                nonce\\n            );\\n            // Increase nonce and execute transaction.\\n            nonce++;\\n            txHash = keccak256(txHashData);\\n            checkSignatures(txHash, txHashData, signatures, true);\\n        }\\n        // We require some gas to emit the events (at least 2500) after the execution and some to perform code until the execution (500)\\n        // We also include the 1/64 in the check that is not send along with a call to counteract potential shortings because of EIP-150\\n        require(gasleft() >= (safeTxGas * 64 / 63).max(safeTxGas + 2500) + 500, \\"Not enough gas to execute safe transaction\\");\\n        // Use scope here to limit variable lifetime and prevent `stack too deep` errors\\n        {\\n            uint256 gasUsed = gasleft();\\n            // If the gasPrice is 0 we assume that nearly all available gas can be used (it is always more than safeTxGas)\\n            // We only substract 2500 (compared to the 3000 before) to ensure that the amount passed is still higher than safeTxGas\\n            success = execute(to, value, data, operation, gasPrice == 0 ? (gasleft() - 2500) : safeTxGas);\\n            gasUsed = gasUsed.sub(gasleft());\\n            // We transfer the calculated tx costs to the tx.origin to avoid sending it to intermediate contracts that have made calls\\n            uint256 payment = 0;\\n            if (gasPrice > 0) {\\n                payment = handlePayment(gasUsed, baseGas, gasPrice, gasToken, refundReceiver);\\n            }\\n            if (success) emit ExecutionSuccess(txHash, payment);\\n            else emit ExecutionFailure(txHash, payment);\\n        }\\n    }\\n\\n    function handlePayment(\\n        uint256 gasUsed,\\n        uint256 baseGas,\\n        uint256 gasPrice,\\n        address gasToken,\\n        address payable refundReceiver\\n    )\\n        private\\n        returns (uint256 payment)\\n    {\\n        // solium-disable-next-line security/no-tx-origin\\n        address payable receiver = refundReceiver == address(0) ? tx.origin : refundReceiver;\\n        if (gasToken == address(0)) {\\n            // For ETH we will only adjust the gas price to not be higher than the actual used gas price\\n            payment = gasUsed.add(baseGas).mul(gasPrice < tx.gasprice ? gasPrice : tx.gasprice);\\n            // solium-disable-next-line security/no-send\\n            require(receiver.send(payment), \\"Could not pay gas costs with ether\\");\\n        } else {\\n            payment = gasUsed.add(baseGas).mul(gasPrice);\\n            require(transferToken(gasToken, receiver, payment), \\"Could not pay gas costs with token\\");\\n        }\\n    }\\n\\n    /**\\n    * @dev Checks whether the signature provided is valid for the provided data, hash. Will revert otherwise.\\n    * @param dataHash Hash of the data (could be either a message hash or transaction hash)\\n    * @param data That should be signed (this is passed to an external validator contract)\\n    * @param signatures Signature data that should be verified. Can be ECDSA signature, contract signature (EIP-1271) or approved hash.\\n    * @param consumeHash Indicates that in case of an approved hash the storage can be freed to save gas\\n    */\\n    function checkSignatures(bytes32 dataHash, bytes memory data, bytes memory signatures, bool consumeHash)\\n        internal\\n    {\\n        // Load threshold to avoid multiple storage loads\\n        uint256 _threshold = threshold;\\n        // Check that a threshold is set\\n        require(_threshold > 0, \\"Threshold needs to be defined!\\");\\n        // Check that the provided signature data is not too short\\n        require(signatures.length >= _threshold.mul(65), \\"Signatures data too short\\");\\n        // There cannot be an owner with address 0.\\n        address lastOwner = address(0);\\n        address currentOwner;\\n        uint8 v;\\n        bytes32 r;\\n        bytes32 s;\\n        uint256 i;\\n        for (i = 0; i < _threshold; i++) {\\n            (v, r, s) = signatureSplit(signatures, i);\\n            // If v is 0 then it is a contract signature\\n            if (v == 0) {\\n                // When handling contract signatures the address of the contract is encoded into r\\n                currentOwner = address(uint256(r));\\n\\n                // Check that signature data pointer (s) is not pointing inside the static part of the signatures bytes\\n                // This check is not completely accurate, since it is possible that more signatures than the threshold are send.\\n                // Here we only check that the pointer is not pointing inside the part that is being processed\\n                require(uint256(s) >= _threshold.mul(65), \\"Invalid contract signature location: inside static part\\");\\n\\n                // Check that signature data pointer (s) is in bounds (points to the length of data -> 32 bytes)\\n                require(uint256(s).add(32) <= signatures.length, \\"Invalid contract signature location: length not present\\");\\n\\n                // Check if the contract signature is in bounds: start of data is s + 32 and end is start + signature length\\n                uint256 contractSignatureLen;\\n                // solium-disable-next-line security/no-inline-assembly\\n                assembly {\\n                    contractSignatureLen := mload(add(add(signatures, s), 0x20))\\n                }\\n                require(uint256(s).add(32).add(contractSignatureLen) <= signatures.length, \\"Invalid contract signature location: data not complete\\");\\n\\n                // Check signature\\n                bytes memory contractSignature;\\n                // solium-disable-next-line security/no-inline-assembly\\n                assembly {\\n                    // The signature data for contract signatures is appended to the concatenated signatures and the offset is stored in s\\n                    contractSignature := add(add(signatures, s), 0x20)\\n                }\\n                require(ISignatureValidator(currentOwner).isValidSignature(data, contractSignature) == EIP1271_MAGIC_VALUE, \\"Invalid contract signature provided\\");\\n            // If v is 1 then it is an approved hash\\n            } else if (v == 1) {\\n                // When handling approved hashes the address of the approver is encoded into r\\n                currentOwner = address(uint256(r));\\n                // Hashes are automatically approved by the sender of the message or when they have been pre-approved via a separate transaction\\n                require(msg.sender == currentOwner || approvedHashes[currentOwner][dataHash] != 0, \\"Hash has not been approved\\");\\n                // Hash has been marked for consumption. If this hash was pre-approved free storage\\n                if (consumeHash && msg.sender != currentOwner) {\\n                    approvedHashes[currentOwner][dataHash] = 0;\\n                }\\n            } else if (v > 30) {\\n                // To support eth_sign and similar we adjust v and hash the messageHash with the Ethereum message prefix before applying ecrecover\\n                currentOwner = ecrecover(keccak256(abi.encodePacked(\\"\\\\x19Ethereum Signed Message:\\\\n32\\", dataHash)), v - 4, r, s);\\n            } else {\\n                // Use ecrecover with the messageHash for EOA signatures\\n                currentOwner = ecrecover(dataHash, v, r, s);\\n            }\\n            require (\\n                currentOwner > lastOwner && owners[currentOwner] != address(0) && currentOwner != SENTINEL_OWNERS,\\n                \\"Invalid owner provided\\"\\n            );\\n            lastOwner = currentOwner;\\n        }\\n    }\\n\\n    /// @dev Allows to estimate a Safe transaction.\\n    ///      This method is only meant for estimation purpose, therefore two different protection mechanism against execution in a transaction have been made:\\n    ///      1.) The method can only be called from the safe itself\\n    ///      2.) The response is returned with a revert\\n    ///      When estimating set `from` to the address of the safe.\\n    ///      Since the `estimateGas` function includes refunds, call this method to get an estimated of the costs that are deducted from the safe with `execTransaction`\\n    /// @param to Destination address of Safe transaction.\\n    /// @param value Ether value of Safe transaction.\\n    /// @param data Data payload of Safe transaction.\\n    /// @param operation Operation type of Safe transaction.\\n    /// @return Estimate without refunds and overhead fees (base transaction and payload data gas costs).\\n    function requiredTxGas(address to, uint256 value, bytes calldata data, Enum.Operation operation)\\n        external\\n        authorized\\n        returns (uint256)\\n    {\\n        uint256 startGas = gasleft();\\n        // We don\'t provide an error message here, as we use it to return the estimate\\n        // solium-disable-next-line error-reason\\n        require(execute(to, value, data, operation, gasleft()));\\n        uint256 requiredGas = startGas - gasleft();\\n        // Convert response to string and return via error message\\n        revert(string(abi.encodePacked(requiredGas)));\\n    }\\n\\n    /**\\n    * @dev Marks a hash as approved. This can be used to validate a hash that is used by a signature.\\n    * @param hashToApprove The hash that should be marked as approved for signatures that are verified by this contract.\\n    */\\n    function approveHash(bytes32 hashToApprove)\\n        external\\n    {\\n        require(owners[msg.sender] != address(0), \\"Only owners can approve a hash\\");\\n        approvedHashes[msg.sender][hashToApprove] = 1;\\n        emit ApproveHash(hashToApprove, msg.sender);\\n    }\\n\\n    /**\\n    * @dev Marks a message as signed, so that it can be used with EIP-1271\\n    * @notice Marks a message (`_data`) as signed.\\n    * @param _data Arbitrary length data that should be marked as signed on the behalf of address(this)\\n    */\\n    function signMessage(bytes calldata _data)\\n        external\\n        authorized\\n    {\\n        bytes32 msgHash = getMessageHash(_data);\\n        signedMessages[msgHash] = 1;\\n        emit SignMsg(msgHash);\\n    }\\n\\n    /**\\n    * Implementation of ISignatureValidator (see `interfaces/ISignatureValidator.sol`)\\n    * @dev Should return whether the signature provided is valid for the provided data.\\n    *       The save does not implement the interface since `checkSignatures` is not a view method.\\n    *       The method will not perform any state changes (see parameters of `checkSignatures`)\\n    * @param _data Arbitrary length data signed on the behalf of address(this)\\n    * @param _signature Signature byte array associated with _data\\n    * @return a bool upon valid or invalid signature with corresponding _data\\n    */\\n    function isValidSignature(bytes calldata _data, bytes calldata _signature)\\n        external\\n        returns (bytes4)\\n    {\\n        bytes32 messageHash = getMessageHash(_data);\\n        if (_signature.length == 0) {\\n            require(signedMessages[messageHash] != 0, \\"Hash not approved\\");\\n        } else {\\n            // consumeHash needs to be false, as the state should not be changed\\n            checkSignatures(messageHash, _data, _signature, false);\\n        }\\n        return EIP1271_MAGIC_VALUE;\\n    }\\n\\n    /// @dev Returns hash of a message that can be signed by owners.\\n    /// @param message Message that should be hashed\\n    /// @return Message hash.\\n    function getMessageHash(\\n        bytes memory message\\n    )\\n        public\\n        view\\n        returns (bytes32)\\n    {\\n        bytes32 safeMessageHash = keccak256(\\n            abi.encode(SAFE_MSG_TYPEHASH, keccak256(message))\\n        );\\n        return keccak256(\\n            abi.encodePacked(byte(0x19), byte(0x01), domainSeparator, safeMessageHash)\\n        );\\n    }\\n\\n    /// @dev Returns the bytes that are hashed to be signed by owners.\\n    /// @param to Destination address.\\n    /// @param value Ether value.\\n    /// @param data Data payload.\\n    /// @param operation Operation type.\\n    /// @param safeTxGas Fas that should be used for the safe transaction.\\n    /// @param baseGas Gas costs for data used to trigger the safe transaction.\\n    /// @param gasPrice Maximum gas price that should be used for this transaction.\\n    /// @param gasToken Token address (or 0 if ETH) that is used for the payment.\\n    /// @param refundReceiver Address of receiver of gas payment (or 0 if tx.origin).\\n    /// @param _nonce Transaction nonce.\\n    /// @return Transaction hash bytes.\\n    function encodeTransactionData(\\n        address to,\\n        uint256 value,\\n        bytes memory data,\\n        Enum.Operation operation,\\n        uint256 safeTxGas,\\n        uint256 baseGas,\\n        uint256 gasPrice,\\n        address gasToken,\\n        address refundReceiver,\\n        uint256 _nonce\\n    )\\n        public\\n        view\\n        returns (bytes memory)\\n    {\\n        bytes32 safeTxHash = keccak256(\\n            abi.encode(SAFE_TX_TYPEHASH, to, value, keccak256(data), operation, safeTxGas, baseGas, gasPrice, gasToken, refundReceiver, _nonce)\\n        );\\n        return abi.encodePacked(byte(0x19), byte(0x01), domainSeparator, safeTxHash);\\n    }\\n\\n    /// @dev Returns hash to be signed by owners.\\n    /// @param to Destination address.\\n    /// @param value Ether value.\\n    /// @param data Data payload.\\n    /// @param operation Operation type.\\n    /// @param safeTxGas Fas that should be used for the safe transaction.\\n    /// @param baseGas Gas costs for data used to trigger the safe transaction.\\n    /// @param gasPrice Maximum gas price that should be used for this transaction.\\n    /// @param gasToken Token address (or 0 if ETH) that is used for the payment.\\n    /// @param refundReceiver Address of receiver of gas payment (or 0 if tx.origin).\\n    /// @param _nonce Transaction nonce.\\n    /// @return Transaction hash.\\n    function getTransactionHash(\\n        address to,\\n        uint256 value,\\n        bytes memory data,\\n        Enum.Operation operation,\\n        uint256 safeTxGas,\\n        uint256 baseGas,\\n        uint256 gasPrice,\\n        address gasToken,\\n        address refundReceiver,\\n        uint256 _nonce\\n    )\\n        public\\n        view\\n        returns (bytes32)\\n    {\\n        return keccak256(encodeTransactionData(to, value, data, operation, safeTxGas, baseGas, gasPrice, gasToken, refundReceiver, _nonce));\\n    }\\n}\\n"\r\n    },\r\n    "/gnosis-safe/contracts/base/Executor.sol": {\r\n      "content": "pragma solidity >=0.5.0 <0.7.0;\\nimport \\"../common/Enum.sol\\";\\n\\n\\n/// @title Executor - A contract that can execute transactions\\n/// @author Richard Meissner - <richard@gnosis.pm>\\ncontract Executor {\\n\\n    function execute(address to, uint256 value, bytes memory data, Enum.Operation operation, uint256 txGas)\\n        internal\\n        returns (bool success)\\n    {\\n        if (operation == Enum.Operation.Call)\\n            success = executeCall(to, value, data, txGas);\\n        else if (operation == Enum.Operation.DelegateCall)\\n            success = executeDelegateCall(to, data, txGas);\\n        else\\n            success = false;\\n    }\\n\\n    function executeCall(address to, uint256 value, bytes memory data, uint256 txGas)\\n        internal\\n        returns (bool success)\\n    {\\n        // solium-disable-next-line security/no-inline-assembly\\n        assembly {\\n            success := call(txGas, to, value, add(data, 0x20), mload(data), 0, 0)\\n        }\\n    }\\n\\n    function executeDelegateCall(address to, bytes memory data, uint256 txGas)\\n        internal\\n        returns (bool success)\\n    {\\n        // solium-disable-next-line security/no-inline-assembly\\n        assembly {\\n            success := delegatecall(txGas, to, add(data, 0x20), mload(data), 0, 0)\\n        }\\n    }\\n}\\n"\r\n    },\r\n    "/gnosis-safe/contracts/base/FallbackManager.sol": {\r\n      "content": "pragma solidity >=0.5.0 <0.7.0;\\n\\nimport \\"../common/SelfAuthorized.sol\\";\\n\\n/// @title Fallback Manager - A contract that manages fallback calls made to this contract\\n/// @author Richard Meissner - <richard@gnosis.pm>\\ncontract FallbackManager is SelfAuthorized {\\n\\n    // keccak256(\\"fallback_manager.handler.address\\")\\n    bytes32 internal constant FALLBACK_HANDLER_STORAGE_SLOT = 0x6c9a6c4a39284e37ed1cf53d337577d14212a4870fb976a4366c693b939918d5;\\n\\n    function internalSetFallbackHandler(address handler) internal {\\n        bytes32 slot = FALLBACK_HANDLER_STORAGE_SLOT;\\n        // solium-disable-next-line security/no-inline-assembly\\n        assembly {\\n            sstore(slot, handler)\\n        }\\n    }\\n\\n    /// @dev Allows to add a contract to handle fallback calls.\\n    ///      Only fallback calls without value and with data will be forwarded.\\n    ///      This can only be done via a Safe transaction.\\n    /// @param handler contract to handle fallbacks calls.\\n    function setFallbackHandler(address handler)\\n        public\\n        authorized\\n    {\\n        internalSetFallbackHandler(handler);\\n    }\\n\\n    function ()\\n        external\\n        payable\\n    {\\n        // Only calls without value and with data will be forwarded\\n        if (msg.value > 0 || msg.data.length == 0) {\\n            return;\\n        }\\n        bytes32 slot = FALLBACK_HANDLER_STORAGE_SLOT;\\n        address handler;\\n        // solium-disable-next-line security/no-inline-assembly\\n        assembly {\\n            handler := sload(slot)\\n        }\\n\\n        if (handler != address(0)) {\\n            // solium-disable-next-line security/no-inline-assembly\\n            assembly {\\n                calldatacopy(0, 0, calldatasize())\\n                let success := call(gas, handler, 0, 0, calldatasize(), 0, 0)\\n                returndatacopy(0, 0, returndatasize())\\n                if eq(success, 0) { revert(0, returndatasize()) }\\n                return(0, returndatasize())\\n            }\\n        }\\n    }\\n}"\r\n    },\r\n    "/gnosis-safe/contracts/base/Module.sol": {\r\n      "content": "pragma solidity >=0.5.0 <0.7.0;\\nimport \\"../common/MasterCopy.sol\\";\\nimport \\"./ModuleManager.sol\\";\\n\\n\\n/// @title Module - Base class for modules.\\n/// @author Stefan George - <stefan@gnosis.pm>\\n/// @author Richard Meissner - <richard@gnosis.pm>\\ncontract Module is MasterCopy {\\n\\n    ModuleManager public manager;\\n\\n    modifier authorized() {\\n        require(msg.sender == address(manager), \\"Method can only be called from manager\\");\\n        _;\\n    }\\n\\n    function setManager()\\n        internal\\n    {\\n        // manager can only be 0 at initalization of contract.\\n        // Check ensures that setup function can only be called once.\\n        require(address(manager) == address(0), \\"Manager has already been set\\");\\n        manager = ModuleManager(msg.sender);\\n    }\\n}\\n"\r\n    },\r\n    "/gnosis-safe/contracts/base/ModuleManager.sol": {\r\n      "content": "pragma solidity >=0.5.0 <0.7.0;\\nimport \\"../common/Enum.sol\\";\\nimport \\"../common/SelfAuthorized.sol\\";\\nimport \\"./Executor.sol\\";\\nimport \\"./Module.sol\\";\\n\\n\\n/// @title Module Manager - A contract that manages modules that can execute transactions via this contract\\n/// @author Stefan George - <stefan@gnosis.pm>\\n/// @author Richard Meissner - <richard@gnosis.pm>\\ncontract ModuleManager is SelfAuthorized, Executor {\\n\\n    event EnabledModule(Module module);\\n    event DisabledModule(Module module);\\n    event ExecutionFromModuleSuccess(address indexed module);\\n    event ExecutionFromModuleFailure(address indexed module);\\n\\n    address internal constant SENTINEL_MODULES = address(0x1);\\n\\n    mapping (address => address) internal modules;\\n\\n    function setupModules(address to, bytes memory data)\\n        internal\\n    {\\n        require(modules[SENTINEL_MODULES] == address(0), \\"Modules have already been initialized\\");\\n        modules[SENTINEL_MODULES] = SENTINEL_MODULES;\\n        if (to != address(0))\\n            // Setup has to complete successfully or transaction fails.\\n            require(executeDelegateCall(to, data, gasleft()), \\"Could not finish initialization\\");\\n    }\\n\\n    /// @dev Allows to add a module to the whitelist.\\n    ///      This can only be done via a Safe transaction.\\n    /// @notice Enables the module `module` for the Safe.\\n    /// @param module Module to be whitelisted.\\n    function enableModule(Module module)\\n        public\\n        authorized\\n    {\\n        // Module address cannot be null or sentinel.\\n        require(address(module) != address(0) && address(module) != SENTINEL_MODULES, \\"Invalid module address provided\\");\\n        // Module cannot be added twice.\\n        require(modules[address(module)] == address(0), \\"Module has already been added\\");\\n        modules[address(module)] = modules[SENTINEL_MODULES];\\n        modules[SENTINEL_MODULES] = address(module);\\n        emit EnabledModule(module);\\n    }\\n\\n    /// @dev Allows to remove a module from the whitelist.\\n    ///      This can only be done via a Safe transaction.\\n    /// @notice Disables the module `module` for the Safe.\\n    /// @param prevModule Module that pointed to the module to be removed in the linked list\\n    /// @param module Module to be removed.\\n    function disableModule(Module prevModule, Module module)\\n        public\\n        authorized\\n    {\\n        // Validate module address and check that it corresponds to module index.\\n        require(address(module) != address(0) && address(module) != SENTINEL_MODULES, \\"Invalid module address provided\\");\\n        require(modules[address(prevModule)] == address(module), \\"Invalid prevModule, module pair provided\\");\\n        modules[address(prevModule)] = modules[address(module)];\\n        modules[address(module)] = address(0);\\n        emit DisabledModule(module);\\n    }\\n\\n    /// @dev Allows a Module to execute a Safe transaction without any further confirmations.\\n    /// @param to Destination address of module transaction.\\n    /// @param value Ether value of module transaction.\\n    /// @param data Data payload of module transaction.\\n    /// @param operation Operation type of module transaction.\\n    function execTransactionFromModule(address to, uint256 value, bytes memory data, Enum.Operation operation)\\n        public\\n        returns (bool success)\\n    {\\n        // Only whitelisted modules are allowed.\\n        require(msg.sender != SENTINEL_MODULES && modules[msg.sender] != address(0), \\"Method can only be called from an enabled module\\");\\n        // Execute transaction without further confirmations.\\n        success = execute(to, value, data, operation, gasleft());\\n        if (success) emit ExecutionFromModuleSuccess(msg.sender);\\n        else emit ExecutionFromModuleFailure(msg.sender);\\n    }\\n\\n    /// @dev Allows a Module to execute a Safe transaction without any further confirmations and return data\\n    /// @param to Destination address of module transaction.\\n    /// @param value Ether value of module transaction.\\n    /// @param data Data payload of module transaction.\\n    /// @param operation Operation type of module transaction.\\n    function execTransactionFromModuleReturnData(address to, uint256 value, bytes memory data, Enum.Operation operation)\\n        public\\n        returns (bool success, bytes memory returnData)\\n    {\\n        success = execTransactionFromModule(to, value, data, operation);\\n        // solium-disable-next-line security/no-inline-assembly\\n        assembly {\\n            // Load free memory location\\n            let ptr := mload(0x40)\\n            // We allocate memory for the return data by setting the free memory location to\\n            // current free memory location + data size + 32 bytes for data size value\\n            mstore(0x40, add(ptr, add(returndatasize(), 0x20)))\\n            // Store the size\\n            mstore(ptr, returndatasize())\\n            // Store the data\\n            returndatacopy(add(ptr, 0x20), 0, returndatasize())\\n            // Point the return data to the correct memory location\\n            returnData := ptr\\n        }\\n    }\\n\\n    /// @dev Returns if an module is enabled\\n    /// @return True if the module is enabled\\n    function isModuleEnabled(Module module)\\n        public\\n        view\\n        returns (bool)\\n    {\\n        return SENTINEL_MODULES != address(module) && modules[address(module)] != address(0);\\n    }\\n\\n    /// @dev Returns array of first 10 modules.\\n    /// @return Array of modules.\\n    function getModules()\\n        public\\n        view\\n        returns (address[] memory)\\n    {\\n        (address[] memory array,) = getModulesPaginated(SENTINEL_MODULES, 10);\\n        return array;\\n    }\\n\\n    /// @dev Returns array of modules.\\n    /// @param start Start of the page.\\n    /// @param pageSize Maximum number of modules that should be returned.\\n    /// @return Array of modules.\\n    function getModulesPaginated(address start, uint256 pageSize)\\n        public\\n        view\\n        returns (address[] memory array, address next)\\n    {\\n        // Init array with max page size\\n        array = new address[](pageSize);\\n\\n        // Populate return array\\n        uint256 moduleCount = 0;\\n        address currentModule = modules[start];\\n        while(currentModule != address(0x0) && currentModule != SENTINEL_MODULES && moduleCount < pageSize) {\\n            array[moduleCount] = currentModule;\\n            currentModule = modules[currentModule];\\n            moduleCount++;\\n        }\\n        next = currentModule;\\n        // Set correct size of returned array\\n        // solium-disable-next-line security/no-inline-assembly\\n        assembly {\\n            mstore(array, moduleCount)\\n        }\\n    }\\n}\\n"\r\n    },\r\n    "/gnosis-safe/contracts/base/OwnerManager.sol": {\r\n      "content": "pragma solidity >=0.5.0 <0.7.0;\\nimport \\"../common/SelfAuthorized.sol\\";\\n\\n/// @title OwnerManager - Manages a set of owners and a threshold to perform actions.\\n/// @author Stefan George - <stefan@gnosis.pm>\\n/// @author Richard Meissner - <richard@gnosis.pm>\\ncontract OwnerManager is SelfAuthorized {\\n\\n    event AddedOwner(address owner);\\n    event RemovedOwner(address owner);\\n    event ChangedThreshold(uint256 threshold);\\n\\n    address internal constant SENTINEL_OWNERS = address(0x1);\\n\\n    mapping(address => address) internal owners;\\n    uint256 ownerCount;\\n    uint256 internal threshold;\\n\\n    /// @dev Setup function sets initial storage of contract.\\n    /// @param _owners List of Safe owners.\\n    /// @param _threshold Number of required confirmations for a Safe transaction.\\n    function setupOwners(address[] memory _owners, uint256 _threshold)\\n        internal\\n    {\\n        // Threshold can only be 0 at initialization.\\n        // Check ensures that setup function can only be called once.\\n        require(threshold == 0, \\"Owners have already been setup\\");\\n        // Validate that threshold is smaller than number of added owners.\\n        require(_threshold <= _owners.length, \\"Threshold cannot exceed owner count\\");\\n        // There has to be at least one Safe owner.\\n        require(_threshold >= 1, \\"Threshold needs to be greater than 0\\");\\n        // Initializing Safe owners.\\n        address currentOwner = SENTINEL_OWNERS;\\n        for (uint256 i = 0; i < _owners.length; i++) {\\n            // Owner address cannot be null.\\n            address owner = _owners[i];\\n            require(owner != address(0) && owner != SENTINEL_OWNERS, \\"Invalid owner address provided\\");\\n            // No duplicate owners allowed.\\n            require(owners[owner] == address(0), \\"Duplicate owner address provided\\");\\n            owners[currentOwner] = owner;\\n            currentOwner = owner;\\n        }\\n        owners[currentOwner] = SENTINEL_OWNERS;\\n        ownerCount = _owners.length;\\n        threshold = _threshold;\\n    }\\n\\n    /// @dev Allows to add a new owner to the Safe and update the threshold at the same time.\\n    ///      This can only be done via a Safe transaction.\\n    /// @notice Adds the owner `owner` to the Safe and updates the threshold to `_threshold`.\\n    /// @param owner New owner address.\\n    /// @param _threshold New threshold.\\n    function addOwnerWithThreshold(address owner, uint256 _threshold)\\n        public\\n        authorized\\n    {\\n        // Owner address cannot be null.\\n        require(owner != address(0) && owner != SENTINEL_OWNERS, \\"Invalid owner address provided\\");\\n        // No duplicate owners allowed.\\n        require(owners[owner] == address(0), \\"Address is already an owner\\");\\n        owners[owner] = owners[SENTINEL_OWNERS];\\n        owners[SENTINEL_OWNERS] = owner;\\n        ownerCount++;\\n        emit AddedOwner(owner);\\n        // Change threshold if threshold was changed.\\n        if (threshold != _threshold)\\n            changeThreshold(_threshold);\\n    }\\n\\n    /// @dev Allows to remove an owner from the Safe and update the threshold at the same time.\\n    ///      This can only be done via a Safe transaction.\\n    /// @notice Removes the owner `owner` from the Safe and updates the threshold to `_threshold`.\\n    /// @param prevOwner Owner that pointed to the owner to be removed in the linked list\\n    /// @param owner Owner address to be removed.\\n    /// @param _threshold New threshold.\\n    function removeOwner(address prevOwner, address owner, uint256 _threshold)\\n        public\\n        authorized\\n    {\\n        // Only allow to remove an owner, if threshold can still be reached.\\n        require(ownerCount - 1 >= _threshold, \\"New owner count needs to be larger than new threshold\\");\\n        // Validate owner address and check that it corresponds to owner index.\\n        require(owner != address(0) && owner != SENTINEL_OWNERS, \\"Invalid owner address provided\\");\\n        require(owners[prevOwner] == owner, \\"Invalid prevOwner, owner pair provided\\");\\n        owners[prevOwner] = owners[owner];\\n        owners[owner] = address(0);\\n        ownerCount--;\\n        emit RemovedOwner(owner);\\n        // Change threshold if threshold was changed.\\n        if (threshold != _threshold)\\n            changeThreshold(_threshold);\\n    }\\n\\n    /// @dev Allows to swap/replace an owner from the Safe with another address.\\n    ///      This can only be done via a Safe transaction.\\n    /// @notice Replaces the owner `oldOwner` in the Safe with `newOwner`.\\n    /// @param prevOwner Owner that pointed to the owner to be replaced in the linked list\\n    /// @param oldOwner Owner address to be replaced.\\n    /// @param newOwner New owner address.\\n    function swapOwner(address prevOwner, address oldOwner, address newOwner)\\n        public\\n        authorized\\n    {\\n        // Owner address cannot be null.\\n        require(newOwner != address(0) && newOwner != SENTINEL_OWNERS, \\"Invalid owner address provided\\");\\n        // No duplicate owners allowed.\\n        require(owners[newOwner] == address(0), \\"Address is already an owner\\");\\n        // Validate oldOwner address and check that it corresponds to owner index.\\n        require(oldOwner != address(0) && oldOwner != SENTINEL_OWNERS, \\"Invalid owner address provided\\");\\n        require(owners[prevOwner] == oldOwner, \\"Invalid prevOwner, owner pair provided\\");\\n        owners[newOwner] = owners[oldOwner];\\n        owners[prevOwner] = newOwner;\\n        owners[oldOwner] = address(0);\\n        emit RemovedOwner(oldOwner);\\n        emit AddedOwner(newOwner);\\n    }\\n\\n    /// @dev Allows to update the number of required confirmations by Safe owners.\\n    ///      This can only be done via a Safe transaction.\\n    /// @notice Changes the threshold of the Safe to `_threshold`.\\n    /// @param _threshold New threshold.\\n    function changeThreshold(uint256 _threshold)\\n        public\\n        authorized\\n    {\\n        // Validate that threshold is smaller than number of owners.\\n        require(_threshold <= ownerCount, \\"Threshold cannot exceed owner count\\");\\n        // There has to be at least one Safe owner.\\n        require(_threshold >= 1, \\"Threshold needs to be greater than 0\\");\\n        threshold = _threshold;\\n        emit ChangedThreshold(threshold);\\n    }\\n\\n    function getThreshold()\\n        public\\n        view\\n        returns (uint256)\\n    {\\n        return threshold;\\n    }\\n\\n    function isOwner(address owner)\\n        public\\n        view\\n        returns (bool)\\n    {\\n        return owner != SENTINEL_OWNERS && owners[owner] != address(0);\\n    }\\n\\n    /// @dev Returns array of owners.\\n    /// @return Array of Safe owners.\\n    function getOwners()\\n        public\\n        view\\n        returns (address[] memory)\\n    {\\n        address[] memory array = new address[](ownerCount);\\n\\n        // populate return array\\n        uint256 index = 0;\\n        address currentOwner = owners[SENTINEL_OWNERS];\\n        while(currentOwner != SENTINEL_OWNERS) {\\n            array[index] = currentOwner;\\n            currentOwner = owners[currentOwner];\\n            index ++;\\n        }\\n        return array;\\n    }\\n}\\n"\r\n    },\r\n    "/gnosis-safe/contracts/common/Enum.sol": {\r\n      "content": "pragma solidity >=0.5.0 <0.7.0;\\n\\n\\n/// @title Enum - Collection of enums\\n/// @author Richard Meissner - <richard@gnosis.pm>\\ncontract Enum {\\n    enum Operation {\\n        Call,\\n        DelegateCall\\n    }\\n}\\n"\r\n    },\r\n    "/gnosis-safe/contracts/common/MasterCopy.sol": {\r\n      "content": "pragma solidity >=0.5.0 <0.7.0;\\nimport \\"./SelfAuthorized.sol\\";\\n\\n\\n/// @title MasterCopy - Base for master copy contracts (should always be first super contract)\\n///         This contract is tightly coupled to our proxy contract (see `proxies/GnosisSafeProxy.sol`)\\n/// @author Richard Meissner - <richard@gnosis.io>\\ncontract MasterCopy is SelfAuthorized {\\n\\n    event ChangedMasterCopy(address masterCopy);\\n\\n    // masterCopy always needs to be first declared variable, to ensure that it is at the same location as in the Proxy contract.\\n    // It should also always be ensured that the address is stored alone (uses a full word)\\n    address private masterCopy;\\n\\n    /// @dev Allows to upgrade the contract. This can only be done via a Safe transaction.\\n    /// @param _masterCopy New contract address.\\n    function changeMasterCopy(address _masterCopy)\\n        public\\n        authorized\\n    {\\n        // Master copy address cannot be null.\\n        require(_masterCopy != address(0), \\"Invalid master copy address provided\\");\\n        masterCopy = _masterCopy;\\n        emit ChangedMasterCopy(_masterCopy);\\n    }\\n}\\n"\r\n    },\r\n    "/gnosis-safe/contracts/common/SecuredTokenTransfer.sol": {\r\n      "content": "pragma solidity >=0.5.0 <0.7.0;\\n\\n\\n/// @title SecuredTokenTransfer - Secure token transfer\\n/// @author Richard Meissner - <richard@gnosis.pm>\\ncontract SecuredTokenTransfer {\\n\\n    /// @dev Transfers a token and returns if it was a success\\n    /// @param token Token that should be transferred\\n    /// @param receiver Receiver to whom the token should be transferred\\n    /// @param amount The amount of tokens that should be transferred\\n    function transferToken (\\n        address token,\\n        address receiver,\\n        uint256 amount\\n    )\\n        internal\\n        returns (bool transferred)\\n    {\\n        bytes memory data = abi.encodeWithSignature(\\"transfer(address,uint256)\\", receiver, amount);\\n        // solium-disable-next-line security/no-inline-assembly\\n        assembly {\\n            let success := call(sub(gas, 10000), token, 0, add(data, 0x20), mload(data), 0, 0)\\n            let ptr := mload(0x40)\\n            mstore(0x40, add(ptr, returndatasize()))\\n            returndatacopy(ptr, 0, returndatasize())\\n            switch returndatasize()\\n            case 0 { transferred := success }\\n            case 0x20 { transferred := iszero(or(iszero(success), iszero(mload(ptr)))) }\\n            default { transferred := 0 }\\n        }\\n    }\\n}\\n"\r\n    },\r\n    "/gnosis-safe/contracts/common/SelfAuthorized.sol": {\r\n      "content": "pragma solidity >=0.5.0 <0.7.0;\\n\\n\\n/// @title SelfAuthorized - authorizes current contract to perform actions\\n/// @author Richard Meissner - <richard@gnosis.pm>\\ncontract SelfAuthorized {\\n    modifier authorized() {\\n        require(msg.sender == address(this), \\"Method can only be called from this contract\\");\\n        _;\\n    }\\n}\\n"\r\n    },\r\n    "/gnosis-safe/contracts/common/SignatureDecoder.sol": {\r\n      "content": "pragma solidity >=0.5.0 <0.7.0;\\n\\n\\n/// @title SignatureDecoder - Decodes signatures that a encoded as bytes\\n/// @author Ricardo Guilherme Schmidt (Status Research & Development GmbH)\\n/// @author Richard Meissner - <richard@gnosis.pm>\\ncontract SignatureDecoder {\\n    \\n    /// @dev Recovers address who signed the message\\n    /// @param messageHash operation ethereum signed message hash\\n    /// @param messageSignature message `txHash` signature\\n    /// @param pos which signature to read\\n    function recoverKey (\\n        bytes32 messageHash,\\n        bytes memory messageSignature,\\n        uint256 pos\\n    )\\n        internal\\n        pure\\n        returns (address)\\n    {\\n        uint8 v;\\n        bytes32 r;\\n        bytes32 s;\\n        (v, r, s) = signatureSplit(messageSignature, pos);\\n        return ecrecover(messageHash, v, r, s);\\n    }\\n\\n    /// @dev divides bytes signature into `uint8 v, bytes32 r, bytes32 s`.\\n    /// @notice Make sure to peform a bounds check for @param pos, to avoid out of bounds access on @param signatures\\n    /// @param pos which signature to read. A prior bounds check of this parameter should be performed, to avoid out of bounds access\\n    /// @param signatures concatenated rsv signatures\\n    function signatureSplit(bytes memory signatures, uint256 pos)\\n        internal\\n        pure\\n        returns (uint8 v, bytes32 r, bytes32 s)\\n    {\\n        // The signature format is a compact form of:\\n        //   {bytes32 r}{bytes32 s}{uint8 v}\\n        // Compact means, uint8 is not padded to 32 bytes.\\n        // solium-disable-next-line security/no-inline-assembly\\n        assembly {\\n            let signaturePos := mul(0x41, pos)\\n            r := mload(add(signatures, add(signaturePos, 0x20)))\\n            s := mload(add(signatures, add(signaturePos, 0x40)))\\n            // Here we are loading the last 32 bytes, including 31 bytes\\n            // of \'s\'. There is no \'mload8\' to do this.\\n            //\\n            // \'byte\' is not working due to the Solidity parser, so lets\\n            // use the second best option, \'and\'\\n            v := and(mload(add(signatures, add(signaturePos, 0x41))), 0xff)\\n        }\\n    }\\n}\\n"\r\n    },\r\n    "/gnosis-safe/contracts/external/GnosisSafeMath.sol": {\r\n      "content": "pragma solidity >=0.5.0 <0.7.0;\\n\\n/**\\n * @title GnosisSafeMath\\n * @dev Math operations with safety checks that revert on error\\n * Renamed from SafeMath to GnosisSafeMath to avoid conflicts\\n * TODO: remove once open zeppelin update to solc 0.5.0\\n */\\nlibrary GnosisSafeMath {\\n\\n  /**\\n  * @dev Multiplies two numbers, reverts on overflow.\\n  */\\n  function mul(uint256 a, uint256 b) internal pure returns (uint256) {\\n    // Gas optimization: this is cheaper than requiring \'a\' not being zero, but the\\n    // benefit is lost if \'b\' is also tested.\\n    // See: https://github.com/OpenZeppelin/openzeppelin-solidity/pull/522\\n    if (a == 0) {\\n      return 0;\\n    }\\n\\n    uint256 c = a * b;\\n    require(c / a == b);\\n\\n    return c;\\n  }\\n\\n  /**\\n  * @dev Integer division of two numbers truncating the quotient, reverts on division by zero.\\n  */\\n  function div(uint256 a, uint256 b) internal pure returns (uint256) {\\n    require(b > 0); // Solidity only automatically asserts when dividing by 0\\n    uint256 c = a / b;\\n    // assert(a == b * c + a % b); // There is no case in which this doesn\'t hold\\n\\n    return c;\\n  }\\n\\n  /**\\n  * @dev Subtracts two numbers, reverts on overflow (i.e. if subtrahend is greater than minuend).\\n  */\\n  function sub(uint256 a, uint256 b) internal pure returns (uint256) {\\n    require(b <= a);\\n    uint256 c = a - b;\\n\\n    return c;\\n  }\\n\\n  /**\\n  * @dev Adds two numbers, reverts on overflow.\\n  */\\n  function add(uint256 a, uint256 b) internal pure returns (uint256) {\\n    uint256 c = a + b;\\n    require(c >= a);\\n\\n    return c;\\n  }\\n\\n  /**\\n  * @dev Divides two numbers and returns the remainder (unsigned integer modulo),\\n  * reverts when dividing by zero.\\n  */\\n  function mod(uint256 a, uint256 b) internal pure returns (uint256) {\\n    require(b != 0);\\n    return a % b;\\n  }\\n\\n\\n  /**\\n  * @dev Returns the largest of two numbers.\\n  */\\n  function max(uint256 a, uint256 b) internal pure returns (uint256) {\\n    return a >= b ? a : b;\\n  }\\n}"\r\n    },\r\n    "/gnosis-safe/contracts/interfaces/ISignatureValidator.sol": {\r\n      "content": "pragma solidity >=0.5.0 <0.7.0;\\n\\ncontract ISignatureValidatorConstants {\\n    // bytes4(keccak256(\\"isValidSignature(bytes,bytes)\\")\\n    bytes4 constant internal EIP1271_MAGIC_VALUE = 0x20c13b0b;\\n}\\n\\ncontract ISignatureValidator is ISignatureValidatorConstants {\\n\\n    /**\\n    * @dev Should return whether the signature provided is valid for the provided data\\n    * @param _data Arbitrary length data signed on the behalf of address(this)\\n    * @param _signature Signature byte array associated with _data\\n    *\\n    * MUST return the bytes4 magic value 0x20c13b0b when function passes.\\n    * MUST NOT modify state (using STATICCALL for solc < 0.5, view modifier for solc > 0.5)\\n    * MUST allow external calls\\n    */\\n    function isValidSignature(\\n        bytes memory _data,\\n        bytes memory _signature)\\n        public\\n        view\\n        returns (bytes4);\\n}"\r\n    }\r\n  },\r\n  "settings": {\r\n    "outputSelection": {\r\n      "*": {\r\n        "*": [\r\n          "evm.bytecode",\r\n          "evm.deployedBytecode",\r\n          "abi"\r\n        ]\r\n      }\r\n    }\r\n  }\r\n}}',
        "ABI": '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"owner","type":"address"}],"name":"AddedOwner","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"approvedHash","type":"bytes32"},{"indexed":true,"internalType":"address","name":"owner","type":"address"}],"name":"ApproveHash","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"masterCopy","type":"address"}],"name":"ChangedMasterCopy","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"threshold","type":"uint256"}],"name":"ChangedThreshold","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"contract Module","name":"module","type":"address"}],"name":"DisabledModule","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"contract Module","name":"module","type":"address"}],"name":"EnabledModule","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bytes32","name":"txHash","type":"bytes32"},{"indexed":false,"internalType":"uint256","name":"payment","type":"uint256"}],"name":"ExecutionFailure","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"module","type":"address"}],"name":"ExecutionFromModuleFailure","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"module","type":"address"}],"name":"ExecutionFromModuleSuccess","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bytes32","name":"txHash","type":"bytes32"},{"indexed":false,"internalType":"uint256","name":"payment","type":"uint256"}],"name":"ExecutionSuccess","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"owner","type":"address"}],"name":"RemovedOwner","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"msgHash","type":"bytes32"}],"name":"SignMsg","type":"event"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"constant":true,"inputs":[],"name":"NAME","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"VERSION","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"_threshold","type":"uint256"}],"name":"addOwnerWithThreshold","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"hashToApprove","type":"bytes32"}],"name":"approveHash","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"approvedHashes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_masterCopy","type":"address"}],"name":"changeMasterCopy","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"_threshold","type":"uint256"}],"name":"changeThreshold","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"contract Module","name":"prevModule","type":"address"},{"internalType":"contract Module","name":"module","type":"address"}],"name":"disableModule","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"domainSeparator","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"contract Module","name":"module","type":"address"}],"name":"enableModule","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"},{"internalType":"enum Enum.Operation","name":"operation","type":"uint8"},{"internalType":"uint256","name":"safeTxGas","type":"uint256"},{"internalType":"uint256","name":"baseGas","type":"uint256"},{"internalType":"uint256","name":"gasPrice","type":"uint256"},{"internalType":"address","name":"gasToken","type":"address"},{"internalType":"address","name":"refundReceiver","type":"address"},{"internalType":"uint256","name":"_nonce","type":"uint256"}],"name":"encodeTransactionData","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"},{"internalType":"enum Enum.Operation","name":"operation","type":"uint8"},{"internalType":"uint256","name":"safeTxGas","type":"uint256"},{"internalType":"uint256","name":"baseGas","type":"uint256"},{"internalType":"uint256","name":"gasPrice","type":"uint256"},{"internalType":"address","name":"gasToken","type":"address"},{"internalType":"address payable","name":"refundReceiver","type":"address"},{"internalType":"bytes","name":"signatures","type":"bytes"}],"name":"execTransaction","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"},{"internalType":"enum Enum.Operation","name":"operation","type":"uint8"}],"name":"execTransactionFromModule","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"},{"internalType":"enum Enum.Operation","name":"operation","type":"uint8"}],"name":"execTransactionFromModuleReturnData","outputs":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"bytes","name":"returnData","type":"bytes"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"message","type":"bytes"}],"name":"getMessageHash","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getModules","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"start","type":"address"},{"internalType":"uint256","name":"pageSize","type":"uint256"}],"name":"getModulesPaginated","outputs":[{"internalType":"address[]","name":"array","type":"address[]"},{"internalType":"address","name":"next","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getOwners","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getThreshold","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"},{"internalType":"enum Enum.Operation","name":"operation","type":"uint8"},{"internalType":"uint256","name":"safeTxGas","type":"uint256"},{"internalType":"uint256","name":"baseGas","type":"uint256"},{"internalType":"uint256","name":"gasPrice","type":"uint256"},{"internalType":"address","name":"gasToken","type":"address"},{"internalType":"address","name":"refundReceiver","type":"address"},{"internalType":"uint256","name":"_nonce","type":"uint256"}],"name":"getTransactionHash","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"contract Module","name":"module","type":"address"}],"name":"isModuleEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes","name":"_data","type":"bytes"},{"internalType":"bytes","name":"_signature","type":"bytes"}],"name":"isValidSignature","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"nonce","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"prevOwner","type":"address"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"_threshold","type":"uint256"}],"name":"removeOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"},{"internalType":"enum Enum.Operation","name":"operation","type":"uint8"}],"name":"requiredTxGas","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"handler","type":"address"}],"name":"setFallbackHandler","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address[]","name":"_owners","type":"address[]"},{"internalType":"uint256","name":"_threshold","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"},{"internalType":"address","name":"fallbackHandler","type":"address"},{"internalType":"address","name":"paymentToken","type":"address"},{"internalType":"uint256","name":"payment","type":"uint256"},{"internalType":"address payable","name":"paymentReceiver","type":"address"}],"name":"setup","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"signMessage","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"signedMessages","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"prevOwner","type":"address"},{"internalType":"address","name":"oldOwner","type":"address"},{"internalType":"address","name":"newOwner","type":"address"}],"name":"swapOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]',
        "ContractName": "GnosisSafe",
        "CompilerVersion": "v0.5.17+commit.d19bba13",
        "OptimizationUsed": "0",
        "Runs": "200",
        "ConstructorArguments": "",
        "EVMVersion": "Default",
        "Library": "",
        "LicenseType": "GNU LGPLv3",
        "Proxy": "0",
        "Implementation": "",
        "SwarmSource": "bzzr://eba952a8e826ae22d1831da9d381d7b6c153687b8cb43c646ad31acd2ce84288",
    }
]
